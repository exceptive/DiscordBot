import discord
from discord.ext import commands
from discord import app_commands

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=1343680676792111196)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f"Error syncing commands: {e}")


    
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
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1343680676792111196) # SERVERS ID

@client.tree.command(name="hello", description="Say Hello", guild=GUILD_ID)  #tree commands or slash commands have to be named in lowercase
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Why are you using this command?")

@client.tree.command(name="printer", description="i will print whatever you give me", guild=GUILD_ID)  #tree commands or slash commands have to be named in lowercase
async def hello(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

client.run('MTM0MzY3OTY5ODczOTEzODU2MA.GmympK.1riW1xn9-77RD9E_7d_choeQdyDoJOqy93_E0s')