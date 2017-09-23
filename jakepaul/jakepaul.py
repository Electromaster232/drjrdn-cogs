import discord
from discord.ext import commands

class jakepaul:
    """It's Everyday Bro!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def itseverydaybro (self):
        """IT'S EVERYDAY BRO"""
        await self.bot.say("ITS EVERYDAY BRO! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=hSlb1ezRqfA")
		
    @commands.command()
    async def itseverydaybroparody (self):
        """YO MY NAME IS NICK CROMPTON AND MY COLLAR STAY POPPIN"""
        await self.bot.say("THE ZERO TALENT CREW! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=c3wuf9_ntgU")
		
    @commands.command()
    async def assulted (self):
        """ASSULTED"""
        await self.bot.say("it was more extreme ( ͡° ͜ʖ ͡°) https://youtu.be/DUiD7j6DdVQ?t=12m57s")
		
    @commands.command()
    async def assultedparody (self):
        """PARODY"""
        await self.bot.say("it was more extreme ( ͡° ͜ʖ ͡°) https://youtu.be/txl3ijxkhu4?t=15s")
		
    @commands.command()
    async def fuckjakepaul (self):
        """FUCK HIM"""
        await self.bot.say("FAKE WIFE! FAKE LIFE! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=tCMx_RPLCYc")
		
    @commands.command()
    async def fuckjakepaulreact (self):
        """PEOPLE REACT TO: FUK JAKE PAUL!"""
        await self.bot.say("HACKED BY BANKS! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=5RoNgAVP3K4")
		
    @commands.command()
    async def jakepaulthemesong (self):
        """THEME SONG BROTHA"""
        await self.bot.say("JAKE PAULERS KEEP IT LIT! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=I0Se3ce433Q")
	
    @commands.command()
    async def itseverynightsis (self):
        """EVERY NIGHT"""
        await self.bot.say("ITS EVERYNIGHT SIS! ( ͡° ͜ʖ ͡°) https://www.youtube.com/watch?v=-Zy28mVeVZw")
	
    @commands.command()
    async def dabonhaters (self):
        """DAB ON THE HATERS"""
        await self.bot.say("DAB ON THE HATERS! ( ͡° ͜ʖ ͡°) https://imgur.com/a/CKsco")
	
    @commands.command()
    async def jakepaulpray (self):
        """PRAY"""
        await self.bot.say("https://i.imgur.com/Fndgpwy.png")

def setup(bot):
    bot.add_cog(jakepaul(bot))
