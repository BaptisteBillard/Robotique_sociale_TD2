# coding=utf-8

from naoqi import ALProxy
import sys
import time

robot_ip = "localhost"
robot_port = 53496

engagement_zones = ALProxy("ALEngagementZones", robot_ip, robot_port)
engagement_zones.setFirstLimitDistance(1.0)   # Zone 1 (intime)
engagement_zones.setSecondLimitDistance(2.0)  # Zone 2 (personnelle)
print("Zones d'engagement mises à jour.")

ALMemory = ALProxy("ALMemory", robot_ip, robot_port)
ALDialog = ALProxy("ALDialog", robot_ip, robot_port)
ALTTS = ALProxy("ALTextToSpeech", robot_ip, robot_port)
ALDialog.setLanguage("English")

# writing topics' qichat code as text strings (end-of-line characters are important!)
topic_content = ("topic: ~animal_conversation()\n"
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

topic_name = ALDialog.loadTopicContent(topic_content)
ALDialog.activateTopic(topic_name)
ALDialog.subscribe("engagement_zone_dialog")

print("Zones d'engagement configurées.")

# Callback déclenché lorsqu'une personne entre dans la zone 1
def on_person_enters_zone1(eventName, value, subscriberIdentifier):
    print("Une personne est entrée dans la zone intime !")
    ALTTS.say("Bonjour, tu es très proche de moi. Est-ce que tu veux parler ?")

# S'abonner à l'événement correspondant à l'entrée dans la zone 1
ALMemory.subscribeToEvent("PeoplePerception/PersonEnteredZone1",
                        "pythonScript",
                        "on_person_enters_zone1")

# Garder le programme actif
try:
    print("Attente d'une personne dans la zone 1...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Arrêt du script.")
    ALMemory.unsubscribeToEvent("PeoplePerception/PersonEnteredZone1",
                              "pythonScript")
