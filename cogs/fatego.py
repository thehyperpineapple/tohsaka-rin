import discord
from discord.ext import commands

class mod (commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["fgo"])
    async def fategrandorder(self, ctx):
        embed = discord.Embed(colour=discord.Colour.dark_red(), title="Fate/Grand Order (NA)", description="Commands Dedicated to the Fate/Grand Order game")
        embed.set_image(url="https://imgur.com/VE6ITlD.png")
        embed.set_thumbnail(url="https://imgur.com/KC2QvmL.png")
        embed.add_field(name="beginner", value="Help for beginners", inline=False)
        embed.add_field(name="event", value="Use this command to get a link to view the ongoing and future events", inline=False)
        embed.add_field(name="banners", value="Shows upcoming banner list", inline=False)
        embed.add_field(name="classchart", value="Shows upcoming banner list", inline=False)
        embed.add_field(name="reroll", value="Shows upcoming banner list", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["begin"])
    async def beginner(self, ctx):
        embed = discord.Embed(colour=discord.Colour.dark_red(), title="Beginners Guide to Fate/Grand Order (NA)", description="For new players")
        embed.set_thumbnail(url="https://imgur.com/KC2QvmL.png")
        embed.add_field(name="Rerolling", value="Use this command for more info", inline=False)
        embed.add_field(name="Bind you Account", value="Remember to do this when you start playing the game or else you'd loose your account", inline=False)
        embed.add_field(name="Command Spells", value="Remember you've got Command Spells that regenrate over time so don't feel shy to use them. Avoid SQ team revives", inline=False)
        embed.add_field(name="Tickets", value="Each Month there are 5 tickets available in the shop that can be exchanged with Mana Prisms. Try to get them each month", inline=False)
        embed.add_field(name="Burning Servants", value="Only burn servants if you have them at NP5. Don't burn them unless you've done that", inline=False)
        embed.add_field(name="Limit Breaking Craft Esscences", value="Craft Essences have certain effects while playing. Limit breaking them increases their level cap thus increasing their effects as they increase in levels", inline=False)
        embed.add_field(name="Servant Skills", value="Upgrading Servant Skills are important but it can be done once you've got yourself a decent party", inline=False)
        embed.add_field(name="Playing for Events", value="If there is an event going on focus on it rather than story as events give you a SR Servant once you finish the main quest. You can further get ascension materials and additional copies to increase the NP level. If the event is the rerun then it's your last chance to get them", inline=False)
        embed.add_field(name="Levelling up servants", value="Only use embers(preferably 4 star embers with the same class) for levelling up servants. Do not use other servants to level up others", inline=False)
        embed.add_field(name="Locking Servants", value="Remember to Lock Servants and CEs you use so that you don't accidentally burn them", inline=False)
        embed.add_field(name="Class Advantages", value="Class advantages and disadvantages matter in this game. Use the command `classchart` to get a class affinity chart", inline=False)
        embed.add_field(name="Mash", value="Feed best Kohai with embers. She's good", inline=False)
        embed.add_field(name="Friends", value="Checked pinned messages in this channels for adding friends. Add anyone with a good support in the game so that you can do quests with ease ", inline=False)
        embed.add_field(name="Saint Quartz", value="Save up SQ for servants you really want when their rate-up banner appears. Don't aimlessly burn them", inline=False)
        embed.add_field(name="Finally", value="Have fun while playing the game. Don't rage quit it because of your luck", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["rr"])
    async def reroll(self, ctx):
        embed = discord.Embed(colour=discord.Colour.dark_red(), title="Rerolling", description="The act of starting a new account, using up the resources that are immediately available during the tutorial, and attempting to roll for the best possible combination. If an account doesn't measure up to the target in mind, wipe the app data/cache (or redownload the game) and start over again.Here's a list of servants you want to aim for")
        embed.set_thumbnail(url="https://imgur.com/KC2QvmL.png")
        embed.add_field(name="Siegfried", value="One of the best F2P Dragon Slayer. He can chop up dragons with ease", inline=False)
        embed.add_field(name="Carmilla", value="She does high damage against female servants and is a pretty decent servant", inline=False)
        embed.add_field(name="Elizabeth Báthory", value="She has a high damage NP and several buffs than increase her damage. Her main utility is in buffing female allies by a huge amount", inline=False)
        embed.add_field(name="Emiya", value="He's capable of dealing pretty good AoE damage and well as generating stars", inline=False)
        embed.add_field(name="Martha", value="Saint Martha is pretty useful to remove team debuffs but since this is rare she isn't widely used", inline=False)
        embed.add_field(name="Heracles", value="Illya's BASAKA is a good choice as he can help you clear early stages of the game due to him being of the beserker class", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def banner(self, ctx):
        embed = discord.Embed(colour=discord.Colour.dark_red(), title="Upcoming banners in Fate/Grand Order (NA)", description="Remember to not waste SQ")
        embed.set_thumbnail(url="https://imgur.com/KC2QvmL.png")
        embed.set_image(url="https://imgur.com/CxpAefZ.png")
        await ctx.send(embed = embed)

    @commands.command()
    async def classchart(self, ctx):
        embed = discord.Embed(colour=discord.Colour.dark_red(), title="Class Relationship Chart", description="Adjust your party everytime you're up against enemies")
        embed.set_thumbnail(url="https://imgur.com/KC2QvmL.png")
        embed.set_image(url="https://imgur.com/aMG7KCB.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def event(self, ctx):
        await ctx.send("Here is a link for the Current/Upcoming Events in Fate Grand Order (NA) \nhttps://fategrandorder.fandom.com/wiki/Event_List_(US)")    



def setup(client):
    client.add_cog(mod(client))
