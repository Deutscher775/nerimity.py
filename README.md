# nerimity.py

Python API wrapper for Nerimity originating from [Fiiral](https://github.com/F-iiral), maintained by [Deutscher775](https://github.com/Deutscher775)


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
async def on_ready():
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
