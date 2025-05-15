import requests
from nerimity._enums import ConsoleShortcuts, GlobalClientInformation

class SlashCommand():
    """A class to represent a slash command."""
    def __init__(self, name: str, description: str, args: list = None) -> None:
        self.name = name
        self.description = description
        self.args = args if args else []
    
    @classmethod
    def register(cls, commands: list['SlashCommand']) -> None:
        """Registers all slash commands.
        
        Args:
            commands (list[SlashCommand]): A list of SlashCommand objects to register.
        """
        api_url = f"{GlobalClientInformation.API_URL}/applications/bot/commands"
        
        headers = {
            "Authorization": GlobalClientInformation.TOKEN,
            "Content-Type": "application/json"
        }
        
        data = {
            "commands": [
                {
                    "name": command.name,
                    "description": command.description,
                    "args": command.args
                } for command in commands
            ]
        }
        
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code != 200:
            print(f"{ConsoleShortcuts.error()} Failed to register slash command: {response.text}")
            raise requests.RequestException
        print(f"{ConsoleShortcuts.ok()} Registered {len(commands)} slash commands.")