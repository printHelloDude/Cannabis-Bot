import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Бот активирован')

@bot.command()
async def hola(ctx):
    await ctx.send('Всем здарова, я Cannabis-Bot! Умею чуть больше, чем полное ничего. Вы можете использовать команду: $commands, чтобы посмотреть список всех доступных команд.')

@bot.command()
async def phonkflex1(ctx):
    await ctx.send("https://media4.giphy.com/media/fzZzoftMBR8is/giphy.gif?cid=ecf05e47c0ca0c1fc8b043b0cfe058e8dfac90ce919453b6&rid=giphy.gif")

@bot.command()
async def phonkflex2(ctx):
    await ctx.send("https://media3.giphy.com/media/qTD9EXZRgI1y0/giphy.gif?cid=ecf05e479ea0ae141a7e03a0a7b084604cff29ba935e0ef9&rid=giphy.gif")

@bot.command()
async def phonkflex3(ctx):
    await ctx.send("https://media1.giphy.com/media/5zI213WKIL2uI/giphy.gif?cid=ecf05e4780852270b590dd8bf1621a8e2c9c778f2182fd1f&rid=giphy.gif")

@bot.command()
async def phonkflex4(ctx):
    await ctx.send("https://media0.giphy.com/media/13WBK6FpsXuRtC/giphy.gif?cid=ecf05e47ff59cc7980eec0452430ac4aac4875a31af6fc8e&rid=giphy.gif")

@bot.command()
async def phonkflex5(ctx):
    await ctx.send("https://media4.giphy.com/media/qatu2fd5vCi7C/giphy.gif?cid=ecf05e473524c0be50d587117bcfe74579a90623ac894f2e&rid=giphy.gif")

@bot.command()
async def shitoff(ctx):
    await ctx.send("ВАЖНОЕ ОБЪЯВЛЕНИЕ!")
    await ctx.send("В срочном порядке выключите моргенштерна. Иначе на вас будут наложены штрафные санкции.")

@bot.command()
async def mystery(ctx):
    await ctx.send("https://sun9-8.userapi.com/2iiC_ArvHNXZGQcyY3Yc5aQL5kXAtjUaZA-4mw/h3DKapRlZ_8.jpg")

@bot.command()
async def phonkdrift(ctx):
    await ctx.send("https://www.youtube.com/watch?v=wqnPOILutvs")


@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Список всех команд:", color=0xeee657)

    embed.add_field(name="$commands", value="Вывод всех команд сея бота.", inline=False)
    embed.add_field(name="$hola", value="Приветственный текст.", inline=False)
    embed.add_field(name="$phonkdrift", value="Проще увидеть, чем тут что-то писать.", inline=False)
    embed.add_field(name="$phonkflex1", value="Чисто настоящий флекс под фонк заход первый.", inline=False)
    embed.add_field(name="$phonkflex2", value="Чисто настоящий флекс под фонк заход второй.", inline=False)
    embed.add_field(name="$fphonkflex3", value="Чисто настоящий флекс под фонк заход третий.", inline=False)
    embed.add_field(name="$phonkflex4", value="Чисто настоящий флекс под фонк заход четвертый.", inline=False)
    embed.add_field(name="$phonkflex5", value="Чисто настоящий флекс под фонк заход пятый. Так, ладно. Хватит.", inline=False)
    embed.add_field(name="$shitoff", value="Используйте эту команду, если вы услышали песни моргенштерна.", inline=False)
    embed.add_field(name="$mystery", value="Вы уверены, что хотите узнать чуть больше?", inline=False)

    await ctx.send(embed=embed)

token = os.environ.get('BOT_TOKEN')
bot.run(str(token))