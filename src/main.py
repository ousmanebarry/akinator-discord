import discord
import asyncio
import akinator
from help import help_text
from discord.ext import commands
from setup.setup import token, channel_id
from akinator.async_aki import Akinator
from discord.ext.commands import BucketType


bot = commands.Bot(command_prefix='.',
                   status=discord.Status.online,
                   activity=discord.Game(name='Guess Game'))
aki = Akinator()
emojis_c = ['✅', '❌', '🤷', '👍', '👎', '⏮', '🛑']
emojis_w = ['✅', '❌']
bot.remove_command('help')


def w(name, desc, picture):
    embed_win = discord.Embed(title=f"It's {name} ({desc})! Was I correct?",
                              colour=0x00FF00)
    embed_win.set_image(url=picture)
    return embed_win


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def helpme(ctx):
    desc_helpme = help_text
    embed_var_helpme = discord.Embed(description=desc_helpme, color=0x00FF00)
    await ctx.send(embed=embed_var_helpme)


@bot.command(name='guess')
@commands.max_concurrency(1, per=BucketType.default, wait=False)
async def guess(ctx, *, extra):
    if ctx.channel.id == channel_id:
        desc_loss = ''
        d_loss = ''

        def check_c(reaction, user):
            return user == ctx.author and str(
                reaction.emoji) in emojis_c and reaction.message.content == q

        def check_w(reaction, user):
            return user == ctx.author and str(reaction.emoji) in emojis_w

        async with ctx.typing():
            if extra == 'people':
                q = await aki.start_game(child_mode=True)
            elif extra == 'objects' or extra == 'animals':
                q = await aki.start_game(language=f'en_{extra}',
                                         child_mode=True)
            else:
                title_error_three = 'This game mode does not exist'
                desc_error_three = 'Use **.helpme** to see a list of all the game modes available'
                embed_var_three = discord.Embed(title=title_error_three,
                                                description=desc_error_three,
                                                color=0xFF0000)
                await ctx.reply(embed=embed_var_three)
                return

            embed_question = discord.Embed(
                title=
                'Tip : Wait until all emojis finish being added before reacting'
                ' or you will have to unreact and react again',
                color=0x00FF00)
            await ctx.reply(embed=embed_question)

        while aki.progression <= 85:
            message = await ctx.reply(q)

            for m in emojis_c:
                await message.add_reaction(m)

            try:
                symbol, username = await bot.wait_for('reaction_add',
                                                      timeout=30.0,
                                                      check=check_c)
            except asyncio.TimeoutError:
                embed_game_ended = discord.Embed(
                    title='You took too long,the game has ended',
                    color=0xFF0000)
                await ctx.reply(embed=embed_game_ended)
                return

            if str(symbol) == emojis_c[0]:
                a = 'y'
            elif str(symbol) == emojis_c[1]:
                a = 'n'
            elif str(symbol) == emojis_c[2]:
                a = 'idk'
            elif str(symbol) == emojis_c[3]:
                a = 'p'
            elif str(symbol) == emojis_c[4]:
                a = 'pn'
            elif str(symbol) == emojis_c[5]:
                a = 'b'
            elif str(symbol) == emojis_c[6]:
                embed_game_end = discord.Embed(
                    title='I ended the game because you asked me to do it',
                    color=0x00FF00)
                await ctx.reply(embed=embed_game_end)
                return

            if a == "b":
                try:
                    q = await aki.back()
                except akinator.CantGoBackAnyFurther:
                    pass
            else:
                q = await aki.answer(a)

        await aki.win()

        wm = await ctx.reply(
            embed=w(aki.first_guess['name'], aki.first_guess['description'],
                    aki.first_guess['absolute_picture_path']))

        for e in emojis_w:
            await wm.add_reaction(e)

        try:
            s, u = await bot.wait_for('reaction_add',
                                      timeout=30.0,
                                      check=check_w)
        except asyncio.TimeoutError:
            for times in aki.guesses:
                d_loss = d_loss + times['name'] + '\n'
            t_loss = 'Here is a list of all the people I had in mind :'
            embed_loss = discord.Embed(title=t_loss,
                                       description=d_loss,
                                       color=0xFF0000)
            await ctx.reply(embed=embed_loss)
            return

        if str(s) == emojis_w[0]:
            embed_win = discord.Embed(
                title='Great, guessed right one more time!', color=0x00FF00)
            await ctx.reply(embed=embed_win)
        elif str(s) == emojis_w[1]:
            for times in aki.guesses:
                desc_loss = desc_loss + times['name'] + '\n'
            title_loss = 'No problem, I will win next time! But here is a list of all the people I had in mind :'
            embed_loss = discord.Embed(title=title_loss,
                                       description=desc_loss,
                                       color=0xFF0000)
            await ctx.reply(embed=embed_loss)
    else:
        right_channel = bot.get_channel(channel_id)
        channel_mention = right_channel.mention
        wrong_channel = discord.Embed(
            title='You can only play in the following channel ' +
                  channel_mention,
            color=0xFF0000)
        await ctx.reply(embed=wrong_channel)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        title_error_one = 'You have not entered anything after the command'
        desc_error_one = 'Use **.helpme** to see a list of all the game modes available'
        embed_var_one = discord.Embed(title=title_error_one,
                                      description=desc_error_one,
                                      color=0xFF0000)
        await ctx.reply(embed=embed_var_one)
    if isinstance(error, commands.CommandNotFound):
        title_error_two = 'The command you have entered does not exist'
        desc_error_two = 'Use **.helpme** to see a list of all the commands available'
        embed_var_two = discord.Embed(title=title_error_two,
                                      description=desc_error_two,
                                      color=0xFF0000)
        await ctx.reply(embed=embed_var_two)
    if isinstance(error, commands.MaxConcurrencyReached):
        title_error_four = 'Someone is already playing'
        desc_error_four = 'Please wait until the person currently playing is done with their turn'
        embed_var_four = discord.Embed(title=title_error_four,
                                       description=desc_error_four,
                                       color=0xFF0000)
        await ctx.reply(embed=embed_var_four)


if __name__ == "__main__":
    bot.run(token)
