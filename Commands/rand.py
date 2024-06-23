import random
import disnake
from disnake.ext import commands

class RandomNumber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="rand", description="Generate a random number")
    async def random_number(
        self,
        inter: disnake.ApplicationCommandInteraction,
        min: int = commands.Param(name="min", description="Minimum value", default=0),
        max: int = commands.Param(name="max", description="Maximum value", default=10)
    ):
        if min > max:
            await inter.response.send_message('Error: min should be less than or equal to max')
        else:
            rand_num = random.randint(min, max)
            await inter.response.send_message(f'Random number between {min} and {max}: {rand_num}')

def setup(bot):
    bot.add_cog(RandomNumber(bot))
