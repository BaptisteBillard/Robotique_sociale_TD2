# coding=utf-8

from naoqi import qi
import sys

robot_ip = "localhost"
robot_port = 53496

session = qi.Session()
try:
    session.connect("tcp://{}:{}".format(robot_ip, robot_port))
except RuntimeError:
    print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
            " Run with -h option for help.\n".format(robot_ip, robot_port))
    sys.exit(1)


# Getting the service ALDialog
ALDialog = session.service("ALDialog")
ALDialog.setLanguage("English")

# Get all loaded topic IDs
topics = ALDialog.getAllLoadedTopics()

# Deactivate and unload each topic
for topic_id in topics:
    ALDialog.deactivateTopic(topic_id)
    ALDialog.unloadTopic(topic_id)

# writing topics' qichat code as text strings (end-of-line characters are important!)
topic_content_1 = ("topic: ~animal_conversation()\n"
                    "language: enu\n"
                    "concept:(animal) [cat dog bird fish horse rabbit]\n"
                    "u: (I [like love enjoy] _~animal) That's great! I like $1 too.\n"
                    "u: (do you like _~animal) Yes, I think $1s are very interesting animals.\n"
                    "u: (tell me about _~animal) $1s are wonderful creatures. What do you like about them?\n"
                    "u: (hello) Hello! Do you want to talk about animals?\n"
                    "u: (what animals do you know) I know many animals like cats, dogs, birds, and more.\n"
                    "u: (goodbye) Goodbye! It was nice talking about animals with you.\n"
                    # "recover:\n"
                    # "u: (.*) Sorry, I don't know much about that. Can we talk about animals?\n"
                    )

# Loading the topics directly as text strings
topic_name_1 = ALDialog.loadTopicContent(topic_content_1)

# Activating the loaded topics
ALDialog.activateTopic(topic_name_1)

# Starting the dialog engine - we need to type an arbitrary string as the identifier
# We subscribe only ONCE, regardless of the number of topics we have activated
ALDialog.subscribe('my_dialog_example')

try:
    raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
finally:
    # stopping the dialog engine
    ALDialog.unsubscribe('my_dialog_example')

    # Deactivating all topics
    ALDialog.deactivateTopic(topic_name_1)

    # now that the dialog engine is stopped and there are no more activated topics,
    # we can unload all topics and free the associated memory
    ALDialog.unloadTopic(topic_name_1)

