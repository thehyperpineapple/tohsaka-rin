import discord
import random
from discord.ext import commands


class mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slap(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/rJYqQyKv-.gif",
            "https://cdn.weeb.sh/images/Sk9mfCtY-.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} was slapped!",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def lick(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/rykRHmB6W.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(), description=f"{member.mention} was licked"
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/HJ7lY_QwW.gif",
            "https://cdn.weeb.sh/images/BywGX8caZ.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} was given a hug to help in their fight against depression",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/rkl1xJYDZ.gif",
            "https://cdn.weeb.sh/images/B1SOzCV0W.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} was given a headpat!",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def poke(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/H1fMRpYtb.gif",
            "https://cdn.weeb.sh/images/r1ALxJKwW.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(), description=f"{member.mention} was poked!"
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def stare(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/HyYuG-CBf.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} stared in anger",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["hifi"])
    async def highfive(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/rJenY1XsW.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} was given a highfive",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def greet(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/SyMiVsnCZ.gif",
            "https://cdn.weeb.sh/images/SJvoNshCZ.gif",
            "https://tenor.com/bln55.gif",
            "https://tenor.com/bapEd.gif",
            "https://tenor.com/xNYY.gif",
            "https://tenor.com/4dmK.gif",
            "https://tenor.com/w5qb.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(), description=f"Hello {member.mention}!"
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def bite(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/rJjd1nDLz.gif",
            "https://cdn.weeb.sh/images/rk8illmiW.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} got bit! Yikes you might have an STD",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def handhold(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/SydAx69ZM.gif",
            "https://cdn.weeb.sh/images/BkiRKrLBz.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention}'s hand was held",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def tickle(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/HyPyUymsb.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} was tickled!",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member : discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/r11as1tvZ.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(), description=f"{member.mention} was killed"
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command()
    async def bully(self, ctx, member : discord.Member):
        responses = [
            "https://imgur.com/g005tMV.gif",
            "https://tenor.com/view/mahou-shoujo-site-anime-gif-13078786",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} is being bullied!",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def nou(self, ctx, member : discord.Member):
        responses = [
            "https://imgur.com/4vHTyA0.png",
            "https://imgur.com/JpsfBUk.png",
            "https://imgur.com/d38LlOi.png",
            "https://imgur.com/XRvDfKr.png",
            "https://imgur.com/x2kwbCR.png",
            "https://imgur.com/03xJOlN.png",
            "https://imgur.com/zjBG0L3.png",
            "https://imgur.com/M2ZVe1M.png",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} was no u-ed!",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["misc"])
    async def miscelllaneous(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title="Miscellaneous Commands",
            description="`slap` `lick` `hug` `pat` `poke` `stare` `highfive` `greet` `bite` `handhold` `tickle` `kill` `bully` `nou` ",
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(mod(client))
