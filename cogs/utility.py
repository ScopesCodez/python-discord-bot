# Importing packages and libraries
import disnake
from disnake.ext import commands

# Creating our "Utility" class for the Utility commands category.
class Utility(commands.Cog):
  # Initializing our class.
  def __init__(self, bot):
    self.bot = bot # In cogs, we'll use "self.bot" instead of "bot". For example: `self.bot.latency` and not `bot.latency`.
    
  # Let's make a ping command that shows the bot's latency.
  @commands.command()
  async def ping(self, ctx): # "ctx" is `commands.Context` which is a very powerful class that includes many information about the command's execution.
    # We will create an embed with the title "🏓 Pong!" and the color of the bot's role color and its description is the bot's ping.
    embed = disnake.Embed(title="🏓 Pong!", color=ctx.guild.me.color, description=f"Running on {round(self.bot.latency*1000)}ms")
    # Now we need to send the embed to where the message was executed.
    await ctx.send(embed=embed)
    
  # Now let's make a command that shows your bot's statistics.
  @commands.command(aliases=['botinfo', 'stats']) # We've set an array called "aliases" to create aliases for the command". That way, `!botstats`, `!stats` and `!botinfo` all of them will work.
  async def botstats(self, ctx):
    await ctx.send(f"**Server count:** {len(self.bot.guilds)} servers\n**Users count:** {len(self.bot.users)} users") # We use the character `\n` to create a new line.
    
  # Someone wants to invite your bot, let's make it easy for them!
  @commnads.command()
  async def invite(self, ctx):
    embed = disnake.Embed(description=f"Add me to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot)")
    await ctx.send(embed=embed)

# Now we need to setup this cog to be in your bot's cogs.
def setup(bot):
  bot.add_cog(Utility(bot))
