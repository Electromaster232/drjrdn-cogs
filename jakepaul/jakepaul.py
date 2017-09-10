import discord
from discord.ext import commands

class jakepaul:
    """It's Everyday Bro!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dabonhaters(self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " DO YOU DAB ON THEM HATERS? ( ͡° ͜ʖ ͡°) https://imgur.com/a/CKsco")
		
def setup(bot):
    bot.add_cog(jakepaul(bot))