from mycroft import MycroftSkill, intent_file_handler


class VoiceForm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('form.voice.intent')
    def handle_form_voice(self, message):
        self.speak_dialog('form.voice')


def create_skill():
    return VoiceForm()

