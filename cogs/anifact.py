import discord
from discord.ext import commands
import random

class anifact (commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def anifact(self, ctx):
        facts = ["Spirited Away was the first anime film to be nominated for and win an academy award.",
                 "Sazae-san is the longest-running anime having more than 7500 episodes.",
                 "The anime Space Brothers includes a voice actor that recorded in outer space.",
                 "Animated Japanese films and television shows account for 60% of the world's animation based entertainment.",
                 "The highest grossing anime film of all time is Your Name. ",
                 "Anime is meant for all ages.",
                 "Anime is not the same as cartoon, contrary to popular belief.",
                 "Eucliwood Hellscyth from Is This a Zombie? has 22 different voice actresses.",
                 "Titans in Attack on Titan are based on drunks.",
                 "Everyone In Code Geass Loves Pizza Because The Series Was Funded By Pizza Hut.",
                 "Death Note Inspired Chinese Children To Write Down The Names Of Their Teachers.",
                 "Noragami literally means Stray God.",
                 "Eren's mom lied about her legs being broken to save Eren and Mikasa from the Titans.", 
                 "10% of anime nudgets goes to drawing eyes and bento boxes.",
                 "Angel Beats was originally going to have 26 episodes.",
                 "Kiyoko and Oikawa are the hardest characters to draw in Haikyuu.",
                 "Orange haired characters are full of energy. They are often self-centered troublemakers.",
                 "Oikawa from Haikyuu had a girlfriend who broke up with up beacuse he was too absrobed in Volleyball.",
                 "Shinegami each suffer a tragic death when their Human Lives end.",
                 "Karma from Assassination Classroom has half his phone storage full of Nagisa's Embarrasing Photos.",
                 "If Kuroko had an alternate job it would be a kindergarden teacher.",
                 "Bleach was originally called Snipe and featured Rukia with a Scythe as the main character.",
                 "Muzan is a very good in disguises.",
                 "Nezuko’s Eyes Changed Colors After Her Transformation.",
                 "Bakugo can cook.",
                 "The strongest servant without a hint of doubt is the legendary king of heroes, Gilgamesh.",
                 "For years, Shirou could've died prior to Fate/Stay Night by practicing the most dangerous method of strengthening objects.",
                 "Contrary to the belief of very few Fate/Zero is a prequel to Fate/Stay Night not the original. Fate/Stay Night is divided into 3 routes called Fate, Unlimited Blade Works and Heaven's Feel.",
                 "Izuku Midoriya Is The Ninth One-For-All User.",
                 "Asta was trained by an enemy soldier.",
                 "Yami Sukehiro, Black Bull Captain likes gambling.",
                 "Vanessa has a one-sided flirtatious relationship with her captain, Yami Sukehiro, constantly asking him out to drink with her and to have fun.",
                 "Gilgamesh is a Mage in Fate/Grand Order Absolute Demonic Front Babylonia as he is the living ruler of Uruk at that time.", 
                 "Akira Toriyama forgot about Launch in the Dragon Ball Franchise.",
                 "Zeno-sama destoyed 6 universes because he was bored.",
                 "Patora fussion is said to Be permanent in DBZ but in DBS Vegitto go back to original form.",
                 "Naruto has a DBZ reference. The 4th tail beast is named Son Goku and its Jinchuruki is Roshi.",
                 "God of Destruction die if the respective Supreme Kai is killed.",
                 "4 Universes were excluded from the Tournament of Power. This is because they had a High Mortal Rate.",
                 "Satan from Dragon Ball has actually died many times but it is assumed that he hasn't.",
                 "In 1998 version of HxH Killua saw P*** and asked Gon to join him",
                 "In the manga Killua uses Fire instead of lightening",
                 "In the anime Leorio's main powers has not yet been revealed",
                 "Gon's Ultimate Attack is a reference to Rock, Paper and Scissor",
                 "Natsu's foster father is the Dragon Igneel",
                 "Natsu can absorb any flame without any problem"]
        embed = discord.Embed(colour=discord.Colour.dark_red(), title="Anime Fact", description=f"{random.choice(facts)}")
        embed.set_footer()
        await ctx.send(embed=embed)    



def setup(client):
    client.add_cog(anifact(client))
