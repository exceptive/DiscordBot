import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        if channel:
            await channel.send(f"Welcome {member} to the server! Please checkout the https://discord.com/channels/1343680676792111196/1343681197754286143 for more rules and more")
        else:
            print("No 'welcome' channel found.")

    async def on_message(self, message):
        if message.author == self.user:
            return

        # sends a message when someone reacts to a message (not practical might be removed)
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')

        # sends a message when someone edits a message (not practical might be removed)
    async def on_message_edit(self, before, after):
        await before.channel.send('This messages content was edited')
    
        # message logger in logs
    async def on_message_delete(self, message):
        log_channel = discord.utils.get(message.guild.text_channels, name="logs")
        if log_channel:
            await log_channel.send(f"Message from {message.author} was deleted. The message was: {message.content}")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


client = Client(intents=intents)
client.run('MTM0MzY3OTY5ODczOTEzODU2MA.GmympK.1riW1xn9-77RD9E_7d_choeQdyDoJOqy93_E0s')