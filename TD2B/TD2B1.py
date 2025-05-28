# coding=utf-8

from naoqi import ALProxy

robot_ip = "localhost"
robot_port = 53496

animated_speech = ALProxy("ALAnimatedSpeech", robot_ip, robot_port)

texta = "^start(animations/Stand/Gestures/Think_1)" \
    "Je ne comprends pas très bien." \
    "^wait(animations/Stand/Gestures/Think_1)"
animated_speech.say(texta)

textb = "^start(animations/Stand/Gestures/Enthusiastic_4)" \
    "Super !!" \
    " ^wait(animations/Stand/Gestures/Enthusiastic_4)"
animated_speech.say(textb)

textc = "^start(animations/Stand/Gestures/Sad_1) " \
    "Oh non..." \
    "^wait(animations/Stand/Gestures/Sad_1)"
animated_speech.say(textc)

textd = "^start(animations/Stand/Gestures/Think_4) " \
    "Je ne sais pas..." \
    "^wait(animations/Stand/Gestures/Think_4)"
animated_speech.say(textd)