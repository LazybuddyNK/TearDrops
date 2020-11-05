import discord
from discord.ext import commands
import random
from inputs import responses,fortunes, quo, nerd, tech, rost, bk, cmp, blurt, cf, jk, cfe, chill, cl, ur


class TextCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def magicball(ctx, *, question):
        embed = discord.Embed(title="8Ball :8ball:",
                              colour=discord.Color.magenta())
        embed.add_field(name=f"*Question: {question}*",
                value=f"Conjecture: {random.choice(responses)}")
        await ctx.send(embed=embed)


    @commands.command(aliases=["future"])
    async def fortune(ctx):
        embed = discord.Embed(title='Fortune', color=0x09b58d)
        embed.add_field(name='Your Fortune', value=random.choice(fortunes))
        await ctx.send(embed=embed)


    @commands.command(aliases=['wisdom'])
    async def quote(ctx):
        embed = discord.Embed(title='Quote', color=0x097b5)
        embed.add_field(name='Quote for you', value=f'`{random.choice(quo)}`')
        await ctx.send(embed=embed)


    @commands.command(aliases=['joke','pun'])
    async def dadjoke(ctx):
        embed = discord.Embed(title='Dad joke huh 😏', color=0x5511c2)
        embed.add_field(name=random.choice(jk),
                        value='_looks at you, expecting you to laugh_')
        await ctx.send(embed=embed)

