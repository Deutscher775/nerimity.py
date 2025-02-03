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

## Issues
If you encounter any issues while using the framework feel free to open an [Issue](https://github.com/deutscher775/nerimity.py).
