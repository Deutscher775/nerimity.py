import nerimity


client = nerimity.Client(
    token="MTU5OTEyMDA2NzUzNzMxMzc5Mi0x.1lFB8Rd707bMeldrwpMcUH2hahnqTauawYTYDYOnJoY",
    prefix='!',
)

@client.command(name="testattachment")
async def testattachment(ctx: nerimity.Context, params: str):
    print(params)
    file = await nerimity.Attachment.construct("test.png").upload()
    print(file, file.file_id)
    await ctx.channel.send_message(message_content="Test Attachment", attachment=file)

client.run()

