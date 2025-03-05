import discord
import requests
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
            await channel.send(f"Welcome {member.mention} to the server! Please checkout the https://discord.com/channels/1343680676792111196/1346917332559073384 for more rules and more")
        else:
            print("No 'welcome' channel found.")

    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="goodbye")
        if channel:
            await channel.send(f"Goodbye {member.mention}! We will miss you!")


    async def on_message(self, message):
        if message.author == self.user:
            return

        # sends a message when someone reacts to a message (not practical might be removed)
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')

        # sends a message when someone edits a message (not practical might be removed) (redirecting to logs channel)
    async def on_message_edit(self, before, after):
        log_channel = discord.utils.get(before.guild.text_channels, name="logs")
        if log_channel:
         await log_channel.send(f'a message has been edited by {before.author.mention} was "{before.content}" and now is "{after.content}"')
    
        # message logger in logs
    async def on_message_delete(self, message):
        log_channel = discord.utils.get(message.guild.text_channels, name="logs")
        if log_channel:
            await log_channel.send(f"Message from {message.author.mention} was deleted. The message was: {message.content}")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = Client(command_prefix="!", intents=intents)


 ## slash commands
GUILD_ID = discord.Object(id=1343680676792111196) # SERVERS ID

@client.tree.command(name="hello", description="Say Hello", guild=GUILD_ID)  #tree commands or slash commands have to be named in lowercase
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Why are you using this command?")

@client.tree.command(name="printer", description="i will print whatever you give me", guild=GUILD_ID)  #tree commands or slash commands have to be named in lowercase
async def hello(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

@client.tree.command(name="embed", description="embed demo", guild=GUILD_ID) 
async def hello(interaction: discord.Interaction):
    embed = discord.Embed(title="8BRC check", url="https://www.rolimons.com/item/10159600649", description="views current statistics on 8brc", color=discord.Color.dark_purple())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1343681197754286143/1343681197754286143/8BRC.png")
    embed.add_field(name="Value", value="Field 1 Value", inline=False)
    embed.add_field(name="RAP", value="Put random shit here", inline=False)
    embed.set_footer(text="8-Bit Royal Crown (8BRC)")
    embed.set_author(name=interaction.user.name, url="https://www.rolimons.com/item/10159600649", icon_url="https://tr.rbxcdn.com/180DAY-598f08aea9c33966821949b05a4135c1/420/420/Hat/Png/noFilter")
    await interaction.response.send_message(embed=embed)

#demand mapping for demand display at the limited command
demand_mapping = {
    0: "Terrible",
    1: "Low",
    2: "Normal",
    3: "High",
    4: "Amazing",
    5: "Extreme"
}

@client.tree.command(name="limited", description="Check limited item details", guild=GUILD_ID)
async def limited(interaction: discord.Interaction, item_id: str):
    url = "https://www.rolimons.com/itemapi/itemdetails"
    response = requests.get(url)
    data = response.json()

    if item_id not in data["items"]:
        await interaction.response.send_message("Invalid item ID or item not found.", ephemeral=True)
        return

    item = data["items"][item_id]

    name = item[0]  # Item Name
    acronym = item[1]  # Acronym 
    rap = item[2]  # Recent Average Price
    value = item[3]  # Market Value
    best_price = item[4]  # best price is not working.
    demand = demand_mapping.get(item[5], "Unknown")  # Converts the demand, with the mapping above
    available_copies = item[6]  # Copies Available

    thumbnail_url = f"https://www.rolimons.com/thumbs/{item_id}.png"
    item_url = f"https://www.rolimons.com/item/{item_id}"

    embed = discord.Embed(
        title=name, url=item_url,
        description=f"Statistics for {name} ({acronym})",
        color=discord.Color.dark_red()
    )
    embed.set_thumbnail(url=thumbnail_url)
    embed.add_field(name="Value", value=f"{value:,}" if value != -1 else "N/A", inline=False)
    embed.add_field(name="RAP", value=f"{rap:,}", inline=False)
    embed.add_field(name="Best Price", value=f"{best_price:,}" if best_price != -1 else "N/A", inline=False)
    embed.add_field(name="Demand", value=demand, inline=False)
    embed.add_field(name="Available Copies", value=f"{available_copies:,}", inline=False)
    embed.add_field(name="Acronym", value=acronym, inline=False)
    embed.set_footer(text="Data from Rolimons")
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url if interaction.user.avatar else None)

    await interaction.response.send_message(embed=embed)

client.run('MTM0MzY3OTY5ODczOTEzODU2MA.GmympK.1riW1xn9-77RD9E_7d_choeQdyDoJOqy93_E0s')