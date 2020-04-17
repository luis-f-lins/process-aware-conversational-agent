from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class BookedFlight(Action):
    def name(self):
        return "flight_booked"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("flight_booked", True)]

class BookedHotel(Action):
    def name(self):
        return "hotel_booked"

    def run(self, dispatcher, tracker, domain):
        allslots = tracker.slots
        if allslots['flight_booked'] == True:
            return [SlotSet("hotel_booked", True)]
        else:
            dispatcher.utter_message(text='I\'m sorry, but you need to book the flight first.')

class BookedTransfer(Action):
    def name(self):
        return "transfer_booked"

    def run(self, dispatcher, tracker, domain):
        allslots = tracker.slots
        if allslots['flight_booked'] == True and allslots['hotel_booked'] == True:
            return [SlotSet("transfer_booked", True)]
        elif allslots['flight_booked'] == True:
            dispatcher.utter_message(text='I\'m sorry, but you need to book the hotel first.')
        else: 
            dispatcher.utter_message(text='I\'m sorry, but you need to book the flight and hotel first.')

class BookedTour(Action):
    def name(self):
        return "tour_booked"

    def run(self, dispatcher, tracker, domain):
        allslots = tracker.slots
        if allslots['flight_booked'] == True:
            return [SlotSet("tour_booked", True)]
        else:
            dispatcher.utter_message(text='I\'m sorry, but you need to book the flight first.')


class WhatsLeft(Action):
    def name(self):
        return "whats_left"

    def run(self, dispatcher, tracker, domain):
        allslots = tracker.slots
        leftslots = []
        templates = {'hotel_booked' : 'book a hotel', 'tour_booked' : 'book a tour', 'transfer_booked' : 'book a transfer'}
        for key, value in allslots.items():
            if value == False:
                leftslots.append(key)
        if (len(leftslots) == 0):
            dispatcher.utter_message(text='Congratulations! You\'re all done!')
            return []
        whatslefttemplate = ''
        for i in range(len(leftslots)):
            thistemplate = leftslots[i]
            if i == len(leftslots) - 1 and len(leftslots) > 1:
                whatslefttemplate += 'and ' + templates[thistemplate]
            elif len(leftslots) == 1:
                whatslefttemplate += templates[thistemplate]
                text = 'Great! Now you just have to ' + whatslefttemplate
                dispatcher.utter_message(text=text)
                return []
            else: 
                whatslefttemplate += templates[thistemplate] + ', '
        text = 'Great! Now you still need to ' + whatslefttemplate
        dispatcher.utter_message(text=text)
        return []