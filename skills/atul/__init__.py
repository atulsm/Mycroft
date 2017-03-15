from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'atulsoman'

LOGGER = getLogger(__name__)


class AtulSkill(MycroftSkill):

    def __init__(self):
        super(AtulSkill, self).__init__(name="AtulSkill")

    def initialize(self):
        atul_intent = IntentBuilder("AtulIntent").\
            require("AtulKeyword").build()
        self.register_intent(atul_intent, self.handle_atul_intent)


        alen_intent = IntentBuilder("AlenIntent").\
            require("AlenKeyword").build()
        self.register_intent(alen_intent, self.handle_alen_intent)

        evan_intent = IntentBuilder("EvanIntent").\
            require("EvanKeyword").build()
        self.register_intent(evan_intent, self.handle_evan_intent)

    def handle_atul_intent(self, message):
        self.speak_dialog("atul")

    def handle_alen_intent(self, message):
        self.speak_dialog("alen")

    def handle_evan_intent(self, message):
        self.speak_dialog("evan")

    def stop(self):
        pass


def create_skill():
    return AtulSkill()
