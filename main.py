import discord
import asyncio
from discord.ext import commands
from datetime import datetime

client = discord.Client()
# bot = commands.Bot


@client.event
async def on_ready():
    print('Login as {}'.format(client.user.name))
    client.loop.create_task((status_task()))


async def status_task():
    await client.change_presence(activity=discord.Game('"Bot by Niffi"'), status=discord.Status.online)


async def time_check():
    await client.wait_until_ready()
    message_channel = client.get_channel(770963080796176394)
    while True:
        now = datetime.strftime(datetime.now(), '%H:%M')
        if now == '15j:00':
            message = await message_channel.send("")
            time = 90
        else:
            time = 1
        await asyncio.sleep(time)

# client.loop.create_task(time_check())

client.run('')


# import discord,random,asyncio,os
# from datetime import datetime
# from discord.ext import commands
#
# bot=commands.Bot(command_prefix='!')
#
# send_time='12:00' #time is in 24hr format
# message_channel_id='438781006267547660' #channel ID to send images to
#
# file_name='some_file.txt' #replace with the name of your file with extension
#
# if os.path.isfile(file_name):
# 		with open(file_name, "r") as f:
# 			message_list = f.read()
# 			message_list = message_list.strip().split("\n")
#
# @bot.event
# async def on_ready():
# 	print(bot.user.name)
# 	print(bot.user.id)
#
# async def time_check():
# 	await bot.wait_until_ready()
# 	message_channel=bot.get_channel(message_channel_id)
# 	while not bot.is_closed:
# 		now=datetime.strftime(datetime.now(),'%H:%M')
# 		if now == send_time:
# 			message= random.choice(message_list)
# 			await bot.send_message(message_channel,message)
# 			time=90
# 		else:
# 			time=1
# 		await asyncio.sleep(time)
#
# bot.loop.create_task(time_check())
#
# bot.run('TOKEN')