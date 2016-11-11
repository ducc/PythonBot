import discord
import time

import yaml

LOG_FORMAT = "[{}] {}#{}: {}"
TIME_FORMAT = "%H:%M:%S"

client = discord.Client()

ready = False


def load_config(file: str):
    f = open(file, "r")
    content = f.read()
    oke = yaml.load(content)
    return oke


@client.event
async def on_ready():
    print("ready!")
    global ready
    ready = True


def log(message: discord.Message):
    t = time.strftime(TIME_FORMAT)
    print(LOG_FORMAT.format(t, message.author.name, message.author.discriminator, message.content))


@client.event
async def on_message(message):
    if not ready:
        return
    log(message)
    if str.lower(message.content) == "!react":
        await client.add_reaction(message, "🚮")


token = load_config("../config.yml").get("token")
print("starting...")
client.run(token)
