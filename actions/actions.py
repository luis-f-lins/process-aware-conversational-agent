from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
import json
import requests
import ast

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from rasa_sdk.events import AllSlotsReset

processKey = 'simple_trip_planning_optional'

class StartProcess(Action):
    def name(self):
        return "start_process"

    def run(self, dispatcher, tracker, domain):
        global taskGetUrl
        global processInstanceGetUrl
        global processInstanceId

        url = 'http://localhost:8080/engine-rest/process-definition/key/' + processKey + '/start'
        postPayload = {"variables": {
            "userWantsToBookATransfer": {"value": False},
            "flightDate": {"value": ''}
        },
        }

        response = requests.post(url, json=postPayload)

        print(response.json())
        processInstanceId = response.json()['id']
        taskGetUrl = 'http://localhost:8080/engine-rest/task?processInstanceId=' + processInstanceId
        processInstanceGetUrl = 'http://localhost:8080/engine-rest/process-instance/' + \
            processInstanceId
        dispatcher.utter_message(text='Okay! Let\'s start the process.')

        return [AllSlotsReset()]


def completeCurrentTaskWithPayload(postPayload):
    global currentTaskId 
    url = 'http://localhost:8080/engine-rest/task/' + currentTaskId + '/complete'
    response = requests.post(url, json=postPayload)
    print(response.text)
    return


class AskUser1Form(FormAction):
    def name(self) -> Text:
        return "askUser1_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["flightDate"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "flightDate": [
                self.from_text(intent=None),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        postPayload = {"variables": {"flightDate": {
            "value": tracker.get_slot("flightDate")}}, "withVariablesInReturn": True}

        completeCurrentTaskWithPayload(postPayload)

        return [FollowupAction("whats_next")]

class AskUser2Form(FormAction):
    def name(self) -> Text:
        return "askUser2_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["userWantsToBookATransfer"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "userWantsToBookATransfer": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        postPayload = {"variables": {"userWantsToBookATransfer": {
            "value": tracker.get_slot("userWantsToBookATransfer")}}, "withVariablesInReturn": True}

        completeCurrentTaskWithPayload(postPayload)

        return [FollowupAction("whats_next")]


class BookFlight(Action):
    def name(self):
        return "book_flight"

    def run(self, dispatcher, tracker, domain):
        taskKey = 'book_flight'

        jsonObj = requests.get(taskGetUrl).json()

        availableTask = None

        for i in jsonObj:
            if i['taskDefinitionKey'] == taskKey:
                availableTask = i

        if availableTask == None:
            dispatcher.utter_message(
                text='I\'m sorry, but this task is not available.')
        else:
            global currentTaskId 
            currentTaskId = availableTask['id']

            return [FollowupAction("askUser1_form")]


class BookHotel(Action):
    def name(self):
        return "book_hotel"

    def run(self, dispatcher, tracker, domain):
        taskKey = 'book_hotel'

        jsonObj = requests.get(taskGetUrl).json()

        availableTask = None

        for i in jsonObj:
            if i['taskDefinitionKey'] == taskKey:
                availableTask = i

        if availableTask == None:
            dispatcher.utter_message(
                text='I\'m sorry, but this task is not available.')
        else:  
            global currentTaskId 
            currentTaskId = availableTask['id']

            return [FollowupAction("askUser2_form")]


class BookTransfer(Action):
    def name(self):
        return "book_transfer"

    def run(self, dispatcher, tracker, domain):
        taskKey = 'book_transfer'

        jsonObj = requests.get(taskGetUrl).json()

        availableTask = None

        for i in jsonObj:
            if i['taskDefinitionKey'] == taskKey:
                availableTask = i

        if availableTask == None:
            dispatcher.utter_message(
                text='I\'m sorry, but this task is not available.')
        else:
            global currentTaskId 
            currentTaskId = availableTask['id']
            postPayload = {}

            url = 'http://localhost:8080/engine-rest/task/' + currentTaskId + '/complete'

            response = requests.post(url, json=postPayload)
            print(response.text)

        return []


class BookTour(Action):
    def name(self):
        return "book_tour"

    def run(self, dispatcher, tracker, domain):
        taskKey = 'book_tour'

        jsonObj = requests.get(taskGetUrl).json()

        availableTask = None

        for i in jsonObj:
            if i['taskDefinitionKey'] == taskKey:
                availableTask = i

        if availableTask == None:
            dispatcher.utter_message(
                text='I\'m sorry, but this task is not available.')
        else:
            global currentTaskId 
            currentTaskId = availableTask['id']
            postPayload = {}

            url = 'http://localhost:8080/engine-rest/task/' + currentTaskId + '/complete'

            response = requests.post(url, json=postPayload)
            print(response.text)

        return []


class WhatsNext(Action):
    def name(self):
        return "whats_next"

    def run(self, dispatcher, tracker, domain):
        global templates
        templates = {'book_flight': 'book a flight', 'book_hotel': 'book a hotel',
                     'book_tour': 'book a tour', 'book_transfer': 'book a transfer'}

        jsonObj = requests.get(taskGetUrl).json()

        response = requests.get(processInstanceGetUrl)

        processStillExists = response.status_code

        print(jsonObj)

        if len(jsonObj) > 0:
            dispatcher.utter_message(text='The available tasks are:')
        elif (processStillExists == 404):
            dispatcher.utter_message(text='Congratulations! You\'re all done!')

        for i in jsonObj:
            # if i['description'] != None and "askUser" in i['description']:
            #     return [FollowupAction("ask_user_form")]

            # else:
                utteredMessage = '- ' + templates[i['taskDefinitionKey']]
                dispatcher.utter_message(text=utteredMessage)

        return []
