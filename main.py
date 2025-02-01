import random
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from utils.responses import RESPONSES

load_dotenv()

client = commands.Bot(command_prefix="-")
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online, activity=discord.Game("with Magecraft")
    )
    print("I'm ready to help")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


@client.command()
async def help(ctx):
    embed = discord.Embed(
        colour=discord.Colour.dark_red(),
        title="Help Command",
        description="My prefix is - and this is what I can do",
    )
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.add_field(name="help", value="Displays this Message.", inline=False)
    embed.add_field(
        name="ping", value="I reply with your latency and a pong!", inline=False
    )
    embed.add_field(
        name="8ball",
        value="I could help you make decisions. It's not like I want to!",
        inline=False,
    )
    embed.add_field(
        name="anifact", value="I could interest you with an Anime fact.", inline=False
    )
    embed.add_field(
        name="mod", value="I'll reply with moderation commands.", inline=False
    )
    embed.add_field(
        name="say",
        value="I really don't want to do this but I'll say whatever you want me to!",
        inline=False,
    )
    embed.add_field(
        name="welcome", value="Use this to welcome members to the server!", inline=False
    )
    embed.add_field(
        name="fategrandorder",
        value="I can show a few commands concering Fate/Grand Order",
        inline=False,
    )
    embed.add_field(
        name="miscellaneous",
        value="Kazama baka! This is all because of you!",
        inline=False,
    )
    embed.add_field(
        name="spoiler",
        value="Adds a spoiler tag to attachments",
        inline=False,
    )
    embed.set_footer(text="Programmed by HyperPineapple#0452 © 2020")
    await ctx.send(embed=embed)


@client.command()
async def mod(ctx):
    embed = discord.Embed(
        colour=discord.Colour.dark_red(),
        title="Moderation Commands",
        description="Here are the moderation commands",
    )
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.add_field(
        name="clear", value="I'm going make your messages disappear.", inline=False
    )
    embed.add_field(
        name="kick", value="I'll kick you out if you aren't useful!", inline=False
    )
    embed.add_field(
        name="ban", value="I could ban you from returning here!", inline=False
    )
    embed.add_field(
        name="unban", value="Okay I'm sorry! I'll let you back in.", inline=False
    )
    embed.set_footer(text="Programmed by HyperPineapple#0452 © 2020")
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong `{round(client.latency * 1000)}ms`")


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
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
        "Very doubtful.",
    ]
    await ctx.send(f"{random.choice(responses)}")


@client.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send("{}".format(msg))


# @client.event
# async def on_message(message):
#     # Delete messages without attachments sent in image-only channels
#     image_channels = os.environ["IMAGE_CHANNELS"].split("|")
#     if (
#         str(message.channel.id) in image_channels
#         and not message.attachments
#         and message.content[0] != "\\"
#         and message.content[:4] != "http"
#         and message.content[:5] != "<http"
#     ):
#         await message.delete()
#         return
#     # Delete messages containing blacklisted words
#     # blacklist = os.environ["BLACKLIST"].split("|")
#     # for emoji in blacklist:
#     # if emoji in message.content:
#     # await message.delete()
#     #   return
#     await client.process_commands(message)


@client.event
async def on_message_delete(message):
    image_channels = os.environ["IMAGE_CHANNELS"].split("|")
    if (
        str(message.channel.id) in image_channels
        and not message.attachments
        and message.content[0] != "\\"
        and message.content != "!spoiler"
        and message.content[:4] != "http"
        and message.content[:5] != "<http"
    ):
        return
    # Delete messages containing blacklisted words
    blacklist = os.environ["BLACKLIST"].split("|")
    for emoji in blacklist:
        if emoji in message.content:
            return
    kaz = os.getenv("KAZ").split("|")
    if str(message.author).split("#")[0] not in kaz:
        return
    webhooks = await message.channel.webhooks()
    if len(webhooks) == 0:
        webhook = await message.channel.create_webhook(name="kaz")
    else:
        webhook = webhooks[0]
    try:
        username = message.author.nick
    except:
        username = str(message.author).split("#")[0]
    if len(message.content) == 0:
        await webhooks[0].send(
            "I'm a dumbass pleb who just deleted a message for probably no reason, don't mind me",
            username=username,
            avatar_url=message.author.avatar_url,
        )
    else:
        await webhooks[0].send(
            message.content, username=username, avatar_url=message.author.avatar_url
        )

class Spoiler(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.bot = client

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send("An error occurred: {}".format(str(error)))

#image spoiler function
 
@client.command()
async def spoiler(ctx):
    try:
        attachment = ctx.message.attachments[0]
    except IndexError:
        await ctx.message.delete()
        await ctx.send("Attachment not found.")
    # rename image
    attachment.filename = f"SPOILER_{attachment.filename}"
    spoiler_image = await attachment.to_file()
    await ctx.message.delete()
    await ctx.send(f"Sent by {ctx.author.name}")
    await ctx.send(file=spoiler_image)

# Load cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# Anti Val event
TRIGGER_WORDS = [f"<@{int(os.environ['VICTIM_USER'])}>", "boot", "val", "come"]  # Added commas

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    # Check if the message is from the TARGET_USER and contains any trigger word
    if message.author.id == int(os.environ['TARGET_USER']) and any(word in message.content.lower() for word in TRIGGER_WORDS):
        await message.channel.send(f"{message.author.mention}, {random.choice(RESPONSES)}")
    
    await client.process_commands(message)  # Ensure commands are processed


client.run(os.environ["TOKEN"])

