import discord
from discord.ext import commands


class mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command
    async def slap(ctx, member: discord.Member):
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

    @commands.command
    async def lick(ctx, member: discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/rykRHmB6W.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(), description=f"{member.mention} was licked"
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command
    async def hug(ctx, member: discord.Member):
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

    @commands.command
    async def pat(ctx, member: discord.Member):
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

    @commands.command
    async def poke(ctx, member: discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/H1fMRpYtb.gif",
            "https://cdn.weeb.sh/images/r1ALxJKwW.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(), description=f"{member.mention} was poked!"
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command
    async def stare(ctx, member: discord.Member):
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
    async def highfive(ctx, member: discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/rJenY1XsW.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} was given a highfive",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command
    async def greet(ctx, member: discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/SyMiVsnCZ.gif",
            "https://cdn.weeb.sh/images/SJvoNshCZ.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(), description=f"Hello {member.mention}!"
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command
    async def bite(ctx, member: discord.Member):
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

    @commands.command
    async def handhold(ctx, member: discord.Member):
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

    @commands.command
    async def tickle(ctx, member: discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/HyPyUymsb.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} was tickled!",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command
    async def kill(ctx, member: discord.Member):
        responses = [
            "https://cdn.weeb.sh/images/r11as1tvZ.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(), description=f"{member.mention} was killed"
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command
    async def bully(ctx, member: discord.Member):
        responses = [
            "https://imgur.com/g005tMV.gif",
        ]
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            description=f"{member.mention} is being bullied!",
        )
        embed.set_image(url=f"{random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["misc"])
    async def miscelllaneous(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title="Miscellaneous Commands",
            description="`slap` `lick` `hug` `pat` `poke` `stare` `highfive` `greet` `bite` `handhold` `tickle` `kill` `bully` ",
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(mod(client))
