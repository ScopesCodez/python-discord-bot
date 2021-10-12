import disnake
from disnake.ext import commands

class Moderation(commands.Cog):
  def __init__(self):
    pass
    
  # Let's make a command that kicks a person from the server.
  @commands.command()
  @commands.has_permissions(kick_members=True) # That's a check that checks if the user has "kick members" permissions. If they don't, `commands.MissingPermissions` error is raised.
  @commands.bot_has_permissions(kick_members=True) # That checks if the bot has "kick members" permissions. If it doesn't, `commands.BotMissingPermissions` error is raised.
  async def kick(self, ctx, member:disnake.Member, *, reason=None): # We passed member parameter as a disnake.Member object to take a discord member object after the command's context.
    # We first need to check if the bot is able to kick that person. Even if the bot has kick members permissions, there're still some cases where the bot cannot kick someone.
    if member.top_role > ctx.guild.me.top_role: # This checks if the member's roles are higher than the bot's.
      return await ctx.send("This user's highest role is higher than mine!")
    if member == ctx.guild.owner: # If the member is the guild's owner.
      return await ctx.send("I cannot kick the server's owner!")
    if member == ctx.author: # If the member is the command's author.
      return await ctx.send("You cannot kick yourself!")
    if member.top_role == ctx.guild.me.top_role: # If the member's top role is as same as the bot's.
      return await ctx.send("This member's highest role is equal to mine!")
    
    # Now let's try to let the user know that they got kicked via DMs.
    try:
      await member.send(f"You have been kicked from **{ctx.guild.name}**!\nReason: {reason}")
    except:
      pass # If the user has DMs off or the bot couldn't send them a DM at all, it will just pass without doing anything.
    
    await member.kick(reason=reason)
    await ctx.send(f"**{member}** has been kicked!")
    
  @commands.command()
  @commands.has_permissions(ban_members=True)
  @commands.bot_has_permissions(kick_members=True)
  async def kick(self, ctx, member:disnake.Member, *, reason=None):
    if member.top_role > ctx.guild.me.top_role:
      return await ctx.send("This user's highest role is higher than mine!")
    if member == ctx.guild.owner:
      return await ctx.send("I cannot kick the server's owner!")
    if member == ctx.author:
      return await ctx.send("You cannot kick yourself!")
    if member.top_role == ctx.guild.me.top_role:
      return await ctx.send("This member's highest role is equal to mine!")

    try:
      await member.send(f"You have been banned from **{ctx.guild.name}**!\nReason: {reason}")
    except:
      pass
    
    await member.ban(reason=reason)
    await ctx.send(f"**{member}** has been banned!")
    
def setup(bot):
  bot.add_cog(Moderation())
