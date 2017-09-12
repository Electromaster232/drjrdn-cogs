import discord
from discord.ext import commands

class jakepaul:
    """It's Everyday Bro!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dabonhaters(self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " DO YOU DAB ON THEM HATERS? ( ͡° ͜ʖ ͡°) https://imgur.com/a/CKsco")

    @commands.command()
    async def itseverydaybro(self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " ITS EVERYDAY BRO! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=hSlb1ezRqfA")
		
    @commands.command()
    async def fuckjakepaul (self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " FAKE WIFE! FAKE LIFE! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=tCMx_RPLCYc")
		
    @commands.command()
    async def jakepaulthemesong (self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " GOT EVERYDAY BRO ON MY FLIP FLOPS! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=D7_9b20qs1w")		

def setup(bot):
    bot.add_cog(jakepaul(bot))
