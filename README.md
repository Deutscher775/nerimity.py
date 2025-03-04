# nerimity.py

Python API wrapper for Nerimity originating from [Fiiral](https://github.com/F-iiral), maintained by [Deutscher775](https://github.com/Deutscher775)
### **[Nerimity Server](https://nerimity.com/i/493CV)** <br>
For questions, help or anything else feel free to join the **[nerimity.py](https://nerimity.com/i/493CV)** Nerimity server.
# Quick jumps
- **[Current Features](#current-features)** <br>
See the features that the framework currently supports.
- **[Installation](#installation)** <br>
Guide on how to install nerimity.py.
- **[Example Bot](#example-commands-bot)** <br>
An example bot you can directly use.
- **[Use-case-examples](#use-case-examples)** <br>
Many various examples on how to use specific functions.

# Current features
#### Command Handling:
- Define and register commands using the @client.command decorator.
- Execute commands with parameters.
Register event listeners using the @client.listen decorator.
Handle various events such as:
- on_ready
- on_message_create
- on_message_updated
- on_message_deleted
- on_button_clicked
- on_presence_change
- on_reaction_add
- on_member_updated
- on_role_updated
- on_role_deleted
- on_role_created
- on_channel_updated
- on_channel_deleted
- on_channel_created
- on_server_updated
- on_member_join
- on_member_left
- on_server_joined
- on_server_left
- on_friend_request_sent
- on_friend_request_pending
- on_friend_request_accepted
- on_friend_removed
- on_minute_pulse
- on_hour_pulse

#### Message Handling:
- Send messages to channels.
    - add attachments
    - add buttons with custom callback
- Edit and delete messages.
- React and unreact to messages.

#### Attachment Handling:
- Create and upload attachments.
- Deserialize attachments from JSON.

#### Channel Management:
- Update channel information.
- Send messages to channels.
- Get messages from channels.
- Purge messages from channels.
- Deserialize channels from JSON.

#### Context Handling:
- Send messages, remove messages, and react to messages within a command context.

#### Invite Management:
- Create and delete server invites.
- Deserialize invites from JSON.

#### Member Management:
- Follow, unfollow, add friend, remove friend, and send direct messages to members.
- Kick, ban, and unban server members.
- Deserialize members and server members from JSON.

#### Post Management:
- Create, delete, comment on, like, and unlike posts.
- Get comments on posts.
- Deserialize posts from JSON.

#### Role Management:
- Create, update, and delete roles.
- Deserialize roles from JSON.

#### Server Management:
- Get server details and ban list.
- Create, update, and delete channels and roles.
- Create and delete invites.
- Update server members.
- Deserialize servers from JSON.

#### Status Management:
- Change the presence status of the bot.

#### Button Interaction:
- Handle button interactions and send popups.
- Deserialize button interactions from JSON.


# Installation
Currently there is no direct installation method. (WIP)
### Follow these 2 simple steps:
1. Clone the repository
```shell
git clone https://github.com/deutscher775/nerimity.py.git
```
2. Copy the `nerimity` folder and insert it into your workspace. It should look like this:
![Image](./readme-assets/directory-view.png)

### Done!
## Example commands bot
```py
import nerimity


client = nerimity.Client(
    token="YOUR_BOT_TOKEN",
    prefix='!',
)

@client.command(name="ping")
async def ping(ctx: nerimity.Context, params: str):
    await ctx.send("Pong!")


@client.listen("on_ready")
async def on_ready(params):
    print(f"Logged in as {client.account.username}")


client.run()
```

## Use case examples
### Sending an attachment
```py
@client.command(name="testattachment")
async def testattachment(ctx: nerimity.Context, params):
    file = await nerimity.Attachment.construct("test.png").upload()
    result = await ctx.send("Test", attachment=file)
```

### Sending buttons with messages
```py
@client.command(name="testbutton")
async def testbutton(ctx: nerimity.Context, params):
    popup_button = nerimity.Button.construct(label="Popup!", id="popuptestbutton", alert=True)
    async def popup_callback(buttoninteraction: nerimity.ButtonInteraction):
        user = client.get_user(buttoninteraction.userId)
        buttoninteraction.send_popup("Test", f"Hello, {user.username}!")
    await popup_button.set_callback(popup_callback)

    message_button = nerimity.Button.construct(label="Message!", id="messagetestbutton")
    async def message_callback(buttoninteraction: nerimity.ButtonInteraction):
        user = client.get_user(buttoninteraction.userId)
        await ctx.send(f"Hello, {user.username}!")
    await message_button.set_callback(message_callback)
    await ctx.send("Test", buttons=[message_button, popup_button])
```

### Creating a post
```py
@client.command(name="createpost")
async def createpost(ctx: nerimity.Context, params):
    content = ""
    for param in params:
        content += param + " "
    await ctx.send("Creating post with text: " + content)
    post = nerimity.Post.create_post(content)
    print(post)
    await ctx.send("Post created.")
```

### Commenting on a post
```py
@client.command(name="comment")
async def comment(ctx: nerimity.Context, params):
    post_id = int(params[0])
    content = ""
    for param in params[1:]:
        content += param + " "
    post = nerimity.Post.get_post(post_id)
    post.create_comment(content)
    await ctx.send("Commented on post.")
```

### Deleting a post
```py
@client.command(name="deletepost")
async def deletepost(ctx: nerimity.Context, params):
    post_id = int(params[0])
    post = nerimity.Post.get_post(post_id)
    post.delete_post()
    await ctx.send("Deleted post.")
```

## Issues
If you encounter any issues while using the framework feel free to open an [Issue](https://github.com/deutscher775/nerimity.py).