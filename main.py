import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'hello {message.author}! Welcome to the server! Please checkout the https://discord.com/channels/1343680676792111196/1343681197754286143 for more rules and more')

        # sends a message when someone reacts to a message (not practical might be removed)
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')

        # sends a message when someone edits a message (not practical might be removed)
    async def on_message_edit(self, before, after):
        await before.channel.send('This messages content was edited')
    
      # sends message if a member leaves the server
        async def on_member_remove(member):
            print(f"{member.name} left the server.")  # Debugging line

            channel = discord.utils.get(member.guild.text_channels, name="general")
            if channel:
                await channel.send(f"{member.name} has left the server. 😢")
            else:
             print("No 'goodbye' channel found.")



intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run('MTM0MzY3OTY5ODczOTEzODU2MA.GmympK.1riW1xn9-77RD9E_7d_choeQdyDoJOqy93_E0s')

