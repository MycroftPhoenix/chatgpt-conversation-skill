from mycroft import MycroftSkill, intent_file_handler


class ChatgptConversation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('conversation.chatgpt.intent')
    def handle_conversation_chatgpt(self, message):
        self.speak_dialog('conversation.chatgpt')


def create_skill():
    return ChatgptConversation()

