# Importing libraries and packages.
import disnake
from disnake.ext import commands # The commands extension from disnake.
import asyncio
import os

# Enabling intents.
intents = disnake.Intents.default()
# To enable member intents, you first need to go to https://discord.com/developers/applications/your_bot_id/bot
# Then scroll down to "Privileged Gateway Intents" and then toggle the switch of "SERVER MEMBER INTENTS".
# Afterwards, you may enable them in your code like that:
intents.members = True

# Creating our bot instance. It's what will be defining your Discord bot.
bot = commands.Bot(command_prefix="your_prefix", intents=intents)

# Now we want to know once our bot is ready to use.
# We'll create an "on_ready" event that will trigger once the bot's cache is fully loaded and the bot is online.
@bot.event
async def on_ready():
  # First, we need to load our cogs.
  for cog in os.listdir("cogs"): # Loop through each file in your "cogs" directory.
      if cog.endswith(".py"):
          try:
              cog = f"cogs.{cog[:-3]}"
              bot.load_extension(cog) # Load the file as an extension.
          except Exception as e:
              print(f"{cog} failed to load:")
              raise e
  # Now we will make the code let us know once the bot is ready.
  print(f"Logged in as {bot.user}!")             
  # Let's set a status for our bot.
  # It will look like "WATCHING {servers count} SERVERS" and it will update every 1 minute.
  while True:
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.watching, name=f"{len(bot.guilds)} SERVERS"
    ))
    await asyncio.sleep(60) # We sleep for 60 seconds after each status update.
  


bot.run("your bot's token") # Now we run the bot.
