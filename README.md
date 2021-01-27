# Process-Aware Conversational Agent

Millions of people execute processes every day. Processes are intrinsic to our personal and professional lives, from planning a party or scheduling a trip, to hiring new employees or admitting students into a University program. Processes are important for several reasons, including:

- Regulating a set of procedures for the execution of a task, so that its execution is unified among members of a large team; 
- Facilitating the identification of the most important tasks in a list;
- Clarifying the dependencies between tasks, so that they can be executed in the right order; 
- Improving efficiency, both individually and for an entire team, if applicable.

This project is a conversational agent that uses Rasa as the main framework for building the chatbot, and Camunda Engine for process management. Camunda will be responsible for making sure the process execution follows the right sequences, and tracking the current state of the process at any given time.

This project was built using specific versions of each framework, and it is not guaranteed to work with any other versions. They are:
- Rasa 1.8.2
- Rasa SDK 1.8.0
- Camunda Modeler 3.4.1

## Instructions for execution

### Camunda

The first step is starting Camunda Engine. There are some tutorials on how to run Camunda [from Docker](https://docs.camunda.org/manual/7.14/installation/docker/) or [from scratch](https://docs.camunda.org/manual/latest/installation/camunda-bpm-run/). After it is up and running, you need to check `http://localhost:8080/`, to see if the Camunda web page is showing. If it asks for a login, the default user and password is `demo / demo`. If you go to Cockpit and have never used Camunda in your current machine, you should probably see no running process instances, and below Process Definitions, there should be the number 0.

Now, you need to go to Camunda Modeler, load the BPMN file if it's not loaded yet, and then click on the last icon in the toolbar, which should say `Deploy current diagram`. Check if the REST endpoint is pointing to `http://localhost:8080/engine-rest` and `Authentication` is set to `None`. The name can be whichever you prefer. 

Finally, click on the `Deploy` button. When you go back to Camunda Cockpit, you should now see there is 1 Process Definition, and when you click on that number, you should see your process definition key, with 0 running instances. There are no running instances yet because the first one will start running when we ask the chatbot to start the process.

### Rasa

For the Rasa part, we need to open two Terminal windows inside the directory where Rasa files are located. In the first one you should run `rasa run actions`, so it will start the action server. In the other one, you should run `rasa train` and then `rasa shell`, which will start the bot in the command shell. 

It is important to note that, instead of `rasa shell`, you can also use `rasa x` if Rasa X (the default Rasa GUI) is configured, or even `rasa interactive`, which will give you a more in-depth look on why the bot is responding a certain way, if it's behaving in an unexpected manner.

Finally, when the bot is up and running, and you type in a phrase corresponding to the `start_process` intent, it should start a process instance, and you can follow the process execution inside Camunda Cockpit.
