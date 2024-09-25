import discord
import discord.ext.commands   # type: ignore
import bullshit
import asyncio
import discord.ext
import reddit_scrape
import gpt
import traceback
import datetime
import pathlib
import os
import random
import wordfiles as wf
import webscrape
import time
import datetime

VERSION_NUMBER = 0.1

swearwords = ["fuck", "shit", "cunt", "dick", "cum", "piss", "ass", "hell", "cock", "slut", "prick", "bitch", "sex", "nigga", "nigger"]
compliment_comments = []

polling_channel = None

timestamp = time.time()

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        client.loop.create_task(wait_for_poll())

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        message.attachments

        raw_msg = message.content.lower()

        master_user = await client.fetch_user(226412002866757642)
        
        print(message.channel.id)
        if message.author == client.user and message.channel.id == 1282059605320536148:
            await message.add_reaction("✅")
            await message.add_reaction("❔")
            await message.add_reaction("❌")

        if message.author == client.user:
            return
        
        try: 
            
            if raw_msg == "/willysize":
                await message.channel.send(VERSION_NUMBER)

            if raw_msg.find("table") >= 0:
                await message.channel.send("┬─┬")

            for word in swearwords:
                if raw_msg.find(word) >= 0:
                    if bullshit.increase_bullshit_meter(message.author):
                        msg = wf.generate_insult(message.author)
                        await message.channel.send(msg)
                    break
            
            if raw_msg.find("nut") >= 0:
                f = discord.File(open(os.path.join(cur_dir, "elephant.png"),"rb"))
                await message.channel.send(file=f)

            if raw_msg.find("among") >= 0:
                await message.add_reaction("🤨")

            if raw_msg.find("sad") >= 0:
                await message.channel.send(wf.generate_quote())
            '''
            if raw_msg.find("voice") >= 0:
                voice_state = message.author.voice
                if voice_state:
                    await voice_state.channel.connect()
            '''
            global timestamp
            now = time.time()
            if now - timestamp >= 10 and  (raw_msg.find("willy") >= 0 or raw_msg.find(client.get_user(1228039945239924756).mention) >= 0): 
                
                timestamp = time.time()
                
                if wf.sentence_contains_word_in_file("positive_adjectives.txt", raw_msg):
                    await message.reply("{} {}'s on my shi".format(wf.get_random_line_in_file("positive_adjectives.txt"), wf.get_random_line_in_file("nouns.txt")))
                elif wf.sentence_contains_word_in_file("negative_adjectives.txt", raw_msg):
                    await message.reply(wf.get_random_line_in_file("nouns.txt"))
                else:
                    rand = random.randint(1, 10)
                    if rand <= 3:
                        await message.reply(wf.generate_quote())
                    elif rand <= 6:
                        await message.reply("{} {}".format(wf.get_random_line_in_file("positive_adjectives.txt"), wf.get_random_line_in_file("nouns.txt")))
                    elif rand <= 9:
                        await message.reply("{} {}".format(wf.get_random_line_in_file("negative_adjectives.txt"), wf.get_random_line_in_file("nouns.txt")))
                    else:
                        await message.channel.send(webscrape.get_random_wiki_page_first_sentence())
            
            if raw_msg == "raise-error" >= 0:
                raise Exception
            
            if raw_msg.find("wheres the poop") >= 0 and message.author == master_user:
                with open(os.path.join(cur_dir, "logfile.txt"), "r") as f:
                    log_msg = ""
                    for line in f:
                        log_msg += line + "\n"
                    await message.channel.send(log_msg)

        except Exception: 
            print(traceback.format_exc())
            await message.channel.send(master_user.mention+" help i made a stinky")
            with open(os.path.join(cur_dir, "logfile.txt"), "w") as f:
                f.write(str(datetime.datetime.now())+"\n")
                f.write(traceback.format_exc())


async def create_poll_message():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    channel = discord.Client.get_channel(client, 1282059605320536148)
    now = datetime.datetime.now()
    day = now + datetime.timedelta(days=7)
    await channel.send("Poll for **{}**  {}".format(days[int(day.weekday())], str(day.date())))


async def wait_for_poll():
    while True:
        now = datetime.datetime.now()
        if now.hour == 17 and now.minute== 0 and now.second == 0:
            await create_poll_message()
            await asyncio.sleep(1)
        await asyncio.sleep(0.5)


cur_dir = pathlib.Path(__file__).parent.resolve()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

with open(os.path.join(cur_dir, "botkey.txt"), "r") as f:
    botkey = f.readline()

#client.loop.create_task(wait_for_poll())
client.run(botkey)