from nerimity._enums import AttachmentTypes, GlobalClientInformation
import aiohttp
import mimetypes

class Attachment():
    """
    Represents an attachment in Nerimity.

    construct(file_path): static | Creates a new Attachment object from a file path.
    upload(): |coro| Uploads the attachment to the CDN.
    deserialize(): static | Deserialize a json string to a Attachment object.
    """

    def __init__(self) -> None:
        self.internal_type  : int               = None
        self.data_type      : str | None        = None
        self.size           : int | None        = None
        self.data           : str | None        = None
        self.height         : int | None        = None
        self.width          : int | None        = None
        self.name           : str | None        = None
        self.id             : int | None        = None
        self.provider       : str | None        = None
        self.file_id        : str | None        = None
        self.mime           : str | None        = None
        self.created_at     : float | None      = None

    # Public Static: Creates a new Attachment object from a file.
    @staticmethod
    def construct(file_path) -> 'Attachment':
        """Creates a new Attachment object from a file path."""

        new_attachment = Attachment()
        new_attachment.internal_type = AttachmentTypes.OUTGOING

        with open(file_path, 'rb') as file:
            new_attachment.data = file.read()
            new_attachment.data_type, _ = mimetypes.guess_type(file_path)
            new_attachment.size = len(new_attachment.data)
            new_attachment.name = file_path.split("/")[-1] if "/" in file_path else file_path
        
        return new_attachment
    
    # Public: Uploads the attachment to the CDN.
    async def upload(self):
        """|coro| Uploads the attachment to the CDN. Returns the file ID. This is not a usable file yet. It will be automatically uploaded with the send_message method."""
        formdata = aiohttp.FormData()
        formdata.add_field("f", self.data, filename=self.name, content_type=self.data_type)
        headers = {
            "Authorization": GlobalClientInformation.TOKEN,
            }
        async with aiohttp.ClientSession() as session:
            async with session.post(GlobalClientInformation.CDN_URL, headers=headers, data=formdata) as cdn_response:
                json = await cdn_response.json()
                self.file_id = json.get("fileId")
                return self
    
    # Public Static: Deserialize a json string to a Attachment object.
    @staticmethod
    def deserialize(json: dict) -> 'Attachment':
        """Deserialize a json string to a Attachment object."""

        new_attachment = Attachment()
        new_attachment.internal_type    = AttachmentTypes.INCOMING
        new_attachment.height           = json["height"]
        new_attachment.width            = json["width"]
        new_attachment.path             = json["path"]
        new_attachment.id               = int(json["id"])       if json["id"] is not None else None
        new_attachment.provider         = json["provider"]
        new_attachment.file_id          = json["fileId"]
        new_attachment.mime             = json["mime"]
        new_attachment.created_at       = json["createdAt"]

        return new_attachment