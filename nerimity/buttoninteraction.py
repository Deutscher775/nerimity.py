from nerimity.button import Button
import requests
from nerimity._enums import ConsoleShortcuts, GlobalClientInformation

class ButtonInteraction():
    def __init__(self, messageId: int = None, channelId: int = None, button: Button = None, userId: int = None) -> None:
        self.messageId = messageId
        self.channelId = channelId
        self.button = button
        self.userId = userId
    

    def send_popup(self, title: str, content: str) -> None:
        """Sends a popup to the user who clicked the button."""
        api_url = f"{GlobalClientInformation.API_URL}/channels/{self.channelId}/messages/{self.messageId}/buttons/{self.button.id}/callback"

        headers = {
            "Authorization": GlobalClientInformation.TOKEN
        }

        data = {
            "userId": str(self.userId),
            "title": title,
            "content": content
        }

        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code != 200:
            print(f"{ConsoleShortcuts.error} Failed to send popup: {response.text}")

    
    @staticmethod
    def deserialize(json: dict) -> 'ButtonInteraction':
        """Deserialize a json string to a ButtonInteraction object."""
        print(json)
        buttonInteraction = ButtonInteraction()
        buttonInteraction.messageId     = int(json["messageId"])
        buttonInteraction.channelId     = int(json["channelId"])
        buttonInteraction.button        = json["button"]
        buttonInteraction.userId        = int(json["userId"])

        return buttonInteraction

        