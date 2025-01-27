import asyncio

import discord
from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='Use the magic 8 ball to get a random answer', name='8ball')
    async def _8ball(self, ctx, *, question):
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.'
        ]
        await ctx.send(embed=discord.Embed(title="Magic 8 Ball",
                                           description=f'Question: {question}\nAnswer: {random.choice(responses)}',
                                           colour=discord.Colour.blurple()))

    @commands.command(help='Roll a `n` sided die')
    async def roll(self, ctx, sides: int = 6):
        message = await ctx.send(
            embed=discord.Embed(title="Rolling...", description="Rolling a die...", colour=discord.Colour.blurple()))
        await asyncio.sleep(1)
        await message.edit(
            embed=discord.Embed(title="Rolling...", description=f"You rolled a {random.randint(1, sides)}",
                                colour=discord.Colour.blurple()))

    @commands.command(help='Emoji-fy your text')
    async def emoji(self, ctx, *, text):
        await ctx.send(embed=discord.Embed(title="Emoji-fied Text",
                                           description=f"{' '.join([f':regional_indicator_{char.lower()}:' for char in text if char.isalpha()])}",
                                           colour=discord.Colour.blurple()))
async def setup(client):
    await client.add_cog(Fun(client))
