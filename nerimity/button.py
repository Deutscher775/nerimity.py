class Button():
    """Represents a button.
    ## Attributes

    label: string | The label of the button.
    id: string | The ID of the button.
    alert: bool | Whether the button is an alert button. (Button will be red if true)
    """
    def __init__(self) -> None:
        self.label      : str           = None
        self.id         : str           = None
        self.alert      : bool          = False
        self._callback                  = None
    
    @classmethod
    def construct(cls, label: str, id: str, alert: bool = False) -> 'Button':
        """Constructs a button."""
        button = cls()
        button.label = label
        button.id = id
        button.alert = alert
        return button
    
    async def callback(self, buttoninteraction):
        """Callback function for the button."""
        if self._callback:
            await self._callback(buttoninteraction)
    
    async def set_callback(self, callback_func):
        """Sets the callback function for the button."""
        self._callback = callback_func
    
    # Public: Serializes the button to a json string.
    @staticmethod
    def deserialize(json: dict) -> 'Button':
        """Deserialize a json string to a Button object."""
        button = Button()
        button.label        = str(json["label"])
        button.id           = str(json["id"])
        button.alert        = bool(json["alert"])

        return button
