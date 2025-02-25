import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run('MTM0MzY3OTY5ODczOTEzODU2MA.GmympK.1riW1xn9-77RD9E_7d_choeQdyDoJOqy93_E0s')

