from nerimity.button import Button

class ButtonInteraction():
    def __init__(self, messageId: int, channelId: str, button: Button, userId: str):
        self.messageId = messageId
        self.channelId = channelId
        self.button = button
        self.userId = userId

    
    @staticmethod
    def deserialize(json: dict) -> 'ButtonInteraction':
        """Deserialize a json string to a ButtonInteraction object."""
        buttonInteraction = ButtonInteraction()
        buttonInteraction.messageId     = int(json["messageId"])
        buttonInteraction.channelId     = str(json["channelId"])
        buttonInteraction.button        = str(json["button"])
        buttonInteraction.userId        = str(json["userId"])

        return buttonInteraction

        