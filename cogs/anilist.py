import requests
import discord

from discord.ext import commands




def searchChar():
    query = """
    query ($search: String) {
      Character(search: $search) {
        siteUrl
        name {
          full
        }
        media(perPage: 1) {
          nodes {
            title {
                romaji
                english
            }
            siteUrl
          }
        }
        image {
          large
        }
        description(asHtml: true)
      }
    }
    """
    return query


def SearchByID():
    query = """
    query($id: Int, $type: MediaType) {
        Media(id: $id, type: $type) {
        title
        {
            romaji
            english
        }
        siteUrl
        type
        format
        genres
        status
        episodes
        duration
        status
        description(asHtml: true)
        coverImage {
            large
        }
        season
        seasonYear
        startDate {
            day
            month
            year
        }
        averageScore
        favourites
        studios
        {
            edges
            {
                node
                {
                    name
                }
            }
        }
        chapters
        volumes
        hashtag
        }
        }
    """
    return query


def run_query(query, variables):
    request = requests.post(
        "https://graphql.anilist.co", json={"query": query, "variables": variables}
    )
    if request.status_code == 200:
        return request.json()
    elif request.status_code == 404:
        print("Invalid search.")
        return
    else:
        raise Exception(
            "Query failed to run by returning code of {}. {}".format(
                request.status_code, query
            )
        )


def searchStaff():
    query = """
    query ($search: String) {
        Staff(search: $search)
        {
            id
            siteUrl
            name
            {
                full
            }
        image
        {
            large
        }
        characters(sort: FAVOURITES_DESC, perPage: 10) {
        edges
        {
            role
            node
            {
                siteUrl
                name
                {
                    full
                }
            }
        }
    }
    }
    }
    """
    return query


def searchStudio():
    query = """
    query ($search: String) {
    Studio(search: $search) {
        name
        siteUrl
        media (isMain: true, sort: POPULARITY_DESC, perPage: 10) {
            nodes {
                siteUrl
                title {
                    english
                    romaji
                }
            }
        }
    }
}
    """
    return query


def SearchByTitle():
    query = """
    query($search: String, $type: MediaType) {
        Media(search: $search, type: $type) {
        title
        {
            romaji
            english
        }
        siteUrl
        type
        format
        genres
        status
        episodes
        duration
        status
        description(asHtml: true)
        coverImage {
            large
        }
        season
        seasonYear
        startDate {
            day
            month
            year
        }
        averageScore
        favourites
        studios
        {
            edges
            {
                node
                {
                    name
                }
            }
        }
        chapters
        volumes
        hashtag
        }
        }
    """
    return query


def SearchUser():
    query = """
    query ($search: String) {
    User(name: $search) {
        id
        name
        siteUrl
        avatar {
            large
        }
        favourites {
            anime (perPage: 5) {
                nodes {
                siteUrl
                    title {
                        romaji
                        english
                    }
                }
            }
            manga (perPage: 5) {
                nodes {
                siteUrl
                    title {
                        romaji
                        english
                    }
                }
            }
        }
        about (asHtml: true),
        statistics {
            anime {
                minutesWatched
                meanScore
                count
                    }
            manga {
                chaptersRead
                meanScore
                count
            }
        }
    }
    }
    """
    return query


def GetByChar(charName):
    variables = {"search": charName}
    return variables


def GetByID(type, id):
    type = type.upper()
    if type != "ANIME" and type != "MANGA":
        return False
    variables = {"type": type, "id": id}
    return variables


def GetByStaff(staffName):
    variables = {"search": staffName}
    return variables


def GetByStudio(studioName):
    variables = {"search": studioName}
    return variables


def GetByTitle(type, title):
    type = type.upper()
    if type != "ANIME" and type != "MANGA":
        return False
    variables = {"type": type, "search": title}
    return variables


def GetUser(userName):
    variables = {"search": userName}
    return variables


def removeTags(text):
    import re

    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)


def cutLength(text):
    if len(text) > 900:
        return text[:900] + "..."
    return text


def replaceNone(text):
    if text is None:
        return "N/A"
    return text


def animeSearch(title):
    if title.isnumeric():
        query = SearchByID()
        variables = GetByID("anime", title)
    elif not title.isnumeric():
        query = SearchByTitle()
        variables = GetByTitle("anime", title)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(
                description="There does not exist an anime with a title/ID of {}.".format(
                    title
                )
            )

        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title=(
                "{} ({}) {}".format(
                    result["data"]["Media"]["title"]["romaji"],
                    result["data"]["Media"]["title"]["english"],
                    result["data"]["Media"]["format"],
                )
            ),
            url=result["data"]["Media"]["siteUrl"],
            description=(removeTags(result["data"]["Media"]["description"])).replace(
                "&quot;", '"'
            ),
        )
        embed.add_field(
            name="Status", value=result["data"]["Media"]["status"].upper(), inline=True
        )
        embed.add_field(
            name="Season",
            value="{} {}".format(
                result["data"]["Media"]["season"], result["data"]["Media"]["seasonYear"]
            ),
            inline=True,
        )
        embed.add_field(
            name="Number of Episodes",
            value=result["data"]["Media"]["episodes"],
            inline=True,
        )
        embed.add_field(
            name="Duration",
            value="{} minutes/episode".format(
                result["data"]["Media"]["duration"], inline=True
            ),
        )
        embed.add_field(
            name="Favourites", value=result["data"]["Media"]["favourites"], inline=True
        )
        embed.add_field(
            name="Average Score",
            value="{}%".format(result["data"]["Media"]["averageScore"], inline=True),
        )
        embed.set_thumbnail(url=result["data"]["Media"]["coverImage"]["large"])
        return embed


def charSearch(charName):
    query = searchChar()
    variables = GetByChar(charName)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(
                description="There does not exist a character with the name {}.".format(
                    charName
                )
            )

        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title=result["data"]["Character"]["name"]["full"],
            url=result["data"]["Character"]["siteUrl"],
        )

        desc = cutLength(
            removeTags(result["data"]["Character"]["description"]).replace(
                "&quot;", '"'
            )
        )
        for title in result["data"]["Character"]["media"]["nodes"]:
            embed.add_field(
                name="Title of Source",
                value="[{} ({})]({})".format(
                    title["title"]["romaji"],
                    title["title"]["english"],
                    title["siteUrl"],
                    inline=False,
                ),
            )
        embed.add_field(name="Description", value=desc, inline=False)
        embed.set_thumbnail(url=result["data"]["Character"]["image"]["large"])
        return embed


def mangaSearch(title):
    if title.isnumeric():
        query = SearchByID()
        variables = GetByID("manga", title)
    elif not title.isnumeric():
        query = SearchByTitle()
        variables = GetByTitle("manga", title)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(
                description="There does not exist a manga with a title/ID of {}.".format(
                    title
                )
            )

        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title=(
                "{} ({}) {}".format(
                    result["data"]["Media"]["title"]["romaji"],
                    result["data"]["Media"]["title"]["english"],
                    result["data"]["Media"]["format"],
                )
            ),
            url=result["data"]["Media"]["siteUrl"],
            description=(removeTags(result["data"]["Media"]["description"])).replace(
                "&quot;", '"'
            ),
        )

        embed.add_field(
            name="Status", value=result["data"]["Media"]["status"].upper(), inline=True
        )
        embed.add_field(
            name="Start Date",
            value="{}/{}/{}".format(
                result["data"]["Media"]["startDate"]["day"],
                result["data"]["Media"]["startDate"]["month"],
                result["data"]["Media"]["startDate"]["year"],
            ),
            inline=True,
        )
        embed.add_field(
            name="Number of Chapters",
            value=replaceNone(result["data"]["Media"]["chapters"]),
            inline=True,
        )
        embed.add_field(
            name="Number of Volumes",
            value=replaceNone(result["data"]["Media"]["volumes"]),
            inline=True,
        )
        embed.add_field(
            name="Favourites", value=result["data"]["Media"]["favourites"], inline=True
        )
        embed.add_field(
            name="Average Score",
            value="{}".format(
                replaceNone(result["data"]["Media"]["averageScore"]), inline=True
            ),
        )
        embed.set_thumbnail(url=result["data"]["Media"]["coverImage"]["large"])
        return embed


def staffSearch(staffName):
    query = searchStaff()
    variables = GetByStaff(staffName)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(
                description="There does not exist a person with the name {}.".format(
                    staffName
                )
            )

        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title=result["data"]["Staff"]["name"]["full"],
            url=result["data"]["Staff"]["siteUrl"],
        )

        characters = ""

        for char in result["data"]["Staff"]["characters"]["edges"]:
            characters += (
                "[{}]({})".format(char["node"]["name"]["full"], char["node"]["siteUrl"])
                + "\n\n"
            )
        embed.add_field(name="Character List", value=characters)
        embed.set_thumbnail(url=result["data"]["Staff"]["image"]["large"])
        return embed


def studioSearch(studioName):
    query = searchStudio()
    variables = GetByStudio(studioName)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(
                description="There does not exist a studio with a name of {}.".format(
                    studioName
                )
            )

        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title=result["data"]["Studio"]["name"],
            url=result["data"]["Studio"]["siteUrl"],
        )
        studioShows = ""

        for show in result["data"]["Studio"]["media"]["nodes"]:
            studioShows += (
                "[{} ({})]({})".format(
                    (show["title"]["romaji"]),
                    (show["title"]["english"]),
                    show["siteUrl"],
                )
                + "\n\n"
            )
        embed.add_field(
            name="Anime produced by {}".format(result["data"]["Studio"]["name"]),
            value=studioShows,
        )
        return embed


def userError(userName):
    return discord.Embed(
        description="There does not exist a user with the name of {}.".format(userName)
    )


def generateUserInfo(userName):
    result = run_query(SearchUser(), GetUser(userName))
    return result


def userSearch(result):
    try:
        desc = removeTags(result["data"]["User"]["about"]).replace("&quot;", '"')
    except:
        desc = ""

    embedUser = discord.Embed(
        colour=discord.Colour.dark_red(),
        title=result["data"]["User"]["name"],
        url=result["data"]["User"]["siteUrl"],
        description=desc,
    )

    embedUser.add_field(
        name="Total Anime",
        value=result["data"]["User"]["statistics"]["anime"]["count"],
        inline=True,
    )
    embedUser.add_field(
        name="Days Watched",
        value=round(
            int(
                (result["data"]["User"]["statistics"]["anime"]["minutesWatched"]) / 1440
            ),
            1,
        ),
        inline=True,
    )
    embedUser.add_field(
        name="Mean Score",
        value=result["data"]["User"]["statistics"]["anime"]["meanScore"],
        inline=True,
    )

    embedUser.add_field(
        name="Total Manga",
        value=result["data"]["User"]["statistics"]["manga"]["count"],
        inline=True,
    )
    embedUser.add_field(
        name="Chapters Read",
        value=result["data"]["User"]["statistics"]["manga"]["chaptersRead"],
        inline=True,
    )
    embedUser.add_field(
        name="Mean Score",
        value=result["data"]["User"]["statistics"]["manga"]["meanScore"],
        inline=True,
    )
    embedUser.set_thumbnail(url=result["data"]["User"]["avatar"]["large"])
    return embedUser


def userAnime(result):
    aniFav = result["data"]["User"]["favourites"]["anime"]["nodes"]
    embedAni = discord.Embed(colour=discord.Colour.dark_red())

    favs = ""
    if aniFav:
        for fav in result["data"]["User"]["favourites"]["anime"]["nodes"]:
            favs += (
                "[{} ({})]({})".format(
                    (fav["title"]["romaji"]), (fav["title"]["english"]), fav["siteUrl"]
                )
                + "\n\n"
            )
        embedAni.add_field(
            name=("{}'s Favourite Anime".format(result["data"]["User"]["name"])),
            value=favs,
        )
        embedAni.set_thumbnail(url=result["data"]["User"]["avatar"]["large"])
    return embedAni


def userManga(result):
    manFav = result["data"]["User"]["favourites"]["manga"]["nodes"]
    embedMan = discord.Embed(colour=discord.Colour.dark_red())

    favs = ""
    if manFav:
        for fav in result["data"]["User"]["favourites"]["manga"]["nodes"]:
            favs += (
                "[{} ({})]({})".format(
                    (fav["title"]["romaji"]), (fav["title"]["english"]), fav["siteUrl"]
                )
                + "\n\n"
            )
        embedMan.add_field(
            name=("{}'s Favourite Manga".format(result["data"]["User"]["name"])),
            value=favs,
        )
        embedMan.set_thumbnail(url=result["data"]["User"]["avatar"]["large"])
        return embedMan
        
class anilist (commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ANIME", "a"])
    async def anime(self, ctx, *, title):
        embed = animeSearch(title)
        await ctx.send(embed=embed)


    @commands.command(aliases=["MANGA", "m"])
    async def manga(self, ctx, *, title):
        embed = mangaSearch(title)
        await ctx.send(embed=embed)

    @commands.command(aliases=["USER", "u"])
    async def user(self, ctx, *, userName):
        result = generateUserInfo(userName)
        if result:
            try:
                userEmbed = userSearch(result)
                await ctx.send(embed=userEmbed)

                userAnimeEmbed = userAnime(result)
                await ctx.send(embed=userAnimeEmbed)

                userMangaEmbed = userManga(result)
                await ctx.send(embed=userMangaEmbed)

            except HTTPException:
                pass
        else:
            await ctx.send(embed=userError(userName))


    @commands.command(aliases=["STUDIO", "s"])
    async def studio(self, ctx, *, studioName):
        embed = studioSearch(studioName)
        await ctx.send(embed=embed)


    @commands.command(aliases=["STAFF", "st"])
    async def staff(self, ctx, *, staffName):
        embed = staffSearch(staffName)
        await ctx.send(embed=embed)


    @commands.command(aliases=["CHARACTER", "ch", "char"])
    async def character(self, ctx, *, charName):
        embed = charSearch(charName)
        await ctx.send(embed=embed)


    # Help command
    @commands.command()
    async def search(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title="AniList Search Commands",
            description="Anilist Commands",
        )
        embed.add_field(
            name="anime", value="Search anime by title or ID.", inline=False
        )
        embed.add_field(
            name="manga", value="Search manga by title or ID.", inline=False
        )
        embed.add_field(
            name="user",
            value="Search up a user by their username.",
            inline=False,
        )
        embed.add_field(
            name="studio",
            value="Search a studio by their name.",
            inline=False,
        )
        embed.add_field(
            name="char",
            value="Search a character by their name.",
            inline=False,
        )
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(anilist(client))        
