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
    async def everydaybroparody (self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " ZERO TALENT CREW! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=c3wuf9_ntgU")
		
    @commands.command()
    async def fuckjakepaul (self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " FAKE WIFE! FAKE LIFE! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=tCMx_RPLCYc")
		
    @commands.command()
    async def reactfuckjakepaul (self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " HACKED BY BANKS! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=5RoNgAVP3K4")
		
    @commands.command()
    async def jakepaulthemesong (self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " JAKE PAULERS KEEP IT LIT! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=D7_9b20qs1w")
		
    @commands.command()
    async def assulted (self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " it was more extreme ( ͡° ͜ʖ ͡°) https://youtu.be/DUiD7j6DdVQ?t=12m57s")
		
    @commands.command()
    async def assultedparody (self, user : discord.Member):
        
        await self.bot.say("" + user.mention + " it was more extreme ( ͡° ͜ʖ ͡°) https://youtu.be/txl3ijxkhu4?t=15s")

def setup(bot):
    bot.add_cog(jakepaul(bot))
