import random
import discord
from discord.ext import commands, tasks
import os

client = commands.Bot(command_prefix="-")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with Magecraft"))
    print("I'm ready to help")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")



@client.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.dark_red(), title="Help Command", description="My prefix is - and this is what I can do")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.add_field(name="help", value="Displays this Message.", inline=False)
    embed.add_field(name="ping", value="I reply with your latency and a pong!", inline=False)
    embed.add_field(name="8ball", value="I could help you make decisions. It's not like I want to!", inline=False)
    embed.add_field(name="anifact", value="I could interest you with an Anime fact.", inline=False)
    embed.add_field(name="mod", value="I'll reply with moderation commands.", inline=False)
    embed.add_field(name="say", value="I really don't want to do this but I'll say whatever you want me to!", inline=False)
    embed.add_field(name="welcome", value="Use this to eelcome members to the server!", inline=False)
    embed.add_field(name="fategrandorder", value="I can show a few commands concering Fate/Grand Order", inline=False)
    embed.set_footer(text="Programmed by Hyper/Pineapple#0452 © 2020")
    await ctx.send(embed=embed)
    
    
@client.command()
async def mod(ctx):
    embed = discord.Embed(colour=discord.Colour.dark_red(), title="Moderation Commands", description="Here are the moderation commands")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.add_field(name="clear", value="I'm going make your messages disappear.", inline=False)
    embed.add_field(name="kick", value="I'll kick you out if you aren't useful!", inline=False)
    embed.add_field(name="ban", value="I could ban you from returning here!", inline=False)
    embed.add_field(name="unban", value="Okay I'm sorry! I'll let you back in.", inline=False)
    embed.set_footer(text="Programmed by HyperPineapple#0452 © 2020")
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong `{round(client.latency * 1000)}ms`")


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt yes.",
                 "Yes",
                 "Definitely.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "You're getting in the way !",
                 "Better not tell you now.",
                 "I'll nail you in the Medulla Oblongata, so why dont't you go away?",
                 "A First-rate mage like myself could never reply to a loser like you!"
                 "Don’t count on Me !",
                 "My reply is no.",
                 "I don't agree.",
                 "Outlook not so good.",
                 "Very doubtful.",]
    await ctx.send(f"{random.choice(responses)}")

@client.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send("{}" .format(msg))

@client.command()
async def welcome(ctx, member : discord.Member):
    responses=["https://tenor.com/bln55.gif",
               "https://tenor.com/bapEd.gif",
               "https://tenor.com/xNYY.gif",
               "https://tenor.com/4dmK.gif",
               "https://tenor.com/w5qb.gif"]
    await ctx.channel.purge(limit=1)
    await ctx.send(f"Welcome to the Server! {member.mention}")
    await ctx.send(f"{random.choice(responses)}")
    
@client.command()
async def stfu(ctx):
    response=["https://imgur.com/27EwQlQ.png"]
    await ctx.send(f"{random.choice(response)}")

    
@client.command(aliases=["no_u"])
async def nou(ctx, member : discord.Member):
    resp=["https://imgur.com/4vHTyA0.png",
          "https://imgur.com/JpsfBUk.png",
          "https://imgur.com/d38LlOi.png",
          "https://imgur.com/XRvDfKr.png",
          "https://imgur.com/x2kwbCR.png",
          "https://imgur.com/03xJOlN.png",
          "https://imgur.com/zjBG0L3.png",
          "https://imgur.com/M2ZVe1M.png"]
    await ctx.send(f"{member.mention} was no u-ed")
    await ctx.send(f"{random.choice(resp)}")

@client.event
async def on_message(message):
    if ":pinched_fingers" in message.content:
        await client.delete(message)

        for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("NjkxMTk1NTY5NjMyMzEzMzU1.XncdzA.uSeJYDBpyAwDeTrchtnZzwzZ0WI")
