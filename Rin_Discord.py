import random
import discord
from discord.ext import commands, tasks
import os

client = commands.Bot(command_prefix="r/")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with Magic"))
    print("I'm ready to help")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")



@client.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.dark_red(), title="Help Command", description="My prefix is r/ and this is what I can do")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.add_field(name="help", value="Displays this Message.", inline=False)
    embed.add_field(name="ping", value="I reply with your latency and a pong!", inline=False)
    embed.add_field(name="8ball", value="I could help you make decisions. It's not like I want to!", inline=False)
    embed.add_field(name="anifact", value="I could interest you with an Anime fact.", inline=False)
    embed.add_field(name="clear", value="I'm going to show off the Power of the Tohsakas by making your messages disappear.", inline=False)
    embed.add_field(name="kick", value="I'll kick you out if you aren't useful!", inline=False)
    embed.add_field(name="ban", value="I could ban you from returning here!", inline=False)
    embed.add_field(name="unban", value="Okay I'm sorry! I'll let you back in.", inline=False)
    embed.add_field(name="say", value="I really don't want to do this but I'll say whatever you want me to!", inline=False)
    embed.set_footer(text="Programmed by @thehyperpineapple#0452 © 2020")
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
                 "A First-rate mage like myself could never reply to a hack like you!"
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

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("NjkxMTk1NTY5NjMyMzEzMzU1.XncdzA.uSeJYDBpyAwDeTrchtnZzwzZ0WI")
