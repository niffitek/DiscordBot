import discord
import asyncio
from discord.ext import commands
from datetime import datetime
import browse

client = discord.Client()


@client.event
async def on_ready():
    print('Login as {}'.format(client.user.name))
    client.loop.create_task((status_task()))


async def status_task():
    await client.change_presence(activity=discord.Game('"Bot by Niffi"'), status=discord.Status.online)


async def send_message():
    for guild in client.guilds:
        channel = discord.utils.get(guild.channels, name="corona-news")
        channel_id = channel.id
        message_channel = client.get_channel(channel_id)
        message = await channel.send(browse.get_message())


async def time_check():
    await client.wait_until_ready()

    while True:
        now = datetime.strftime(datetime.now(), '%H:%M')
        if now == "9:00":
            await send_message()
            time = 90
        else:
            time = 1
        await asyncio.sleep(time)

client.loop.create_task(time_check())

f = open('token', 'r')
token = f.readline()

client.run(token)  # add Token here
