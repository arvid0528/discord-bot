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

VERSION_NUMBER = 0.2

swearwords = ["fuck", "shit", "cunt", "dick", "cum", "piss", "ass", "hell", "cock", "slut", "prick", "bitch", "sex", "nigga", "nigger"]
compliment_comments = []

polling_channel = None

schedule_channel_id = 1282059605320536148
graph_channel_id = 1291708916073496637
bot_test_channel_id = 1161870771262587012

timestamp = time.time()

async def check_reactions():
    print("Running check_reactions()")
    while True: 
        try:
            go_next_iter = False
            schedule_channel = discord.Client.get_channel(client, schedule_channel_id)
            graph_channel = discord.Client.get_channel(client, graph_channel_id)

            messages = [msg async for msg in schedule_channel.history(limit=7)]
            color_list = [["day", "grey"] for i in range(7)]
            for i in range(len(messages)):
                no_reactions = discord.utils.get(messages[i].reactions, emoji='❌')
                maybe_reactions = discord.utils.get(messages[i].reactions, emoji='❔')
                yes_reactions = discord.utils.get(messages[i].reactions, emoji='✅')
                
                if no_reactions is None or maybe_reactions is None or yes_reactions is None: 
                    await asyncio.sleep(1)
                    go_next_iter = True
                    break
                
                weekday = messages[i].content.split(" ")[2][2:-2]
                color_list[i][0] = weekday
                # only one 'no' is needed to make the day red
                if no_reactions.count > 1:
                    color_list[i][1] = "red"
                    continue
                
                # Not everyone has reacted, keep it grey
                if no_reactions.count + maybe_reactions.count + yes_reactions.count != 6:
                    continue

                if maybe_reactions.count > 1:
                    color_list[i][1] = "orange"
                    continue

                if yes_reactions.count == 4:
                    color_list[i][1] = "green"

            if go_next_iter:
                continue

            color_list.reverse()

            # TODO: Only post new graph if data has changed 
            msg_string = ""
            for daycolor in color_list:
                if daycolor[1] == "red":
                    msg_string += "🟥 "
                elif daycolor[1] == "orange":
                    msg_string += "🟧 "
                elif daycolor[1] == "green":
                    msg_string += "🟩 "
                elif daycolor[1] == "grey":
                    msg_string += "⬜ "
                msg_string += daycolor[0]
                msg_string += "\n"

            last_graph = await graph_channel.fetch_message(graph_channel.last_message_id)
            await last_graph.edit(content=msg_string)
            await asyncio.sleep(10)
        except Exception:
            print(traceback.format_exc())
            bot_test_channel = discord.Client.get_channel(client, bot_test_channel_id)
            await bot_test_channel.send("check_reations crashed: \n " + traceback.format_exc())
            

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        client.loop.create_task(wait_for_poll())
        client.loop.create_task(check_reactions())
        print("exited on_ready()")

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        message.attachments

        raw_msg = message.content

        master_user = await client.fetch_user(226412002866757642)
        
        if message.author == client.user and message.channel.id == schedule_channel_id:
            await message.add_reaction("✅")
            await message.add_reaction("❔")
            await message.add_reaction("❌")

        if message.author == client.user:
            return
        
        try: 
            if message.author == master_user and raw_msg[:7].lower() == "/manual":
                cmd = raw_msg.split(" ")[1].lower()
                arg = raw_msg.split(" ")[2:]
                arg = " ".join(arg)
                if cmd == "send":
                    await message.channel.send(arg)
                elif cmd == "wiki":
                    await message.channel.send(webscrape.get_random_wiki_page_first_sentence())
                elif cmd == "reboot":
                    await message.channel.send("Rebooting...")
                    reboot_system()

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
            
            global timestamp
            now = time.time()
            if now - timestamp >= 10 and  (raw_msg.find("willy") >= 0 or raw_msg.find(client.get_user(1228039945239924756).mention) >= 0): 
                
                timestamp = time.time()
                
                if wf.sentence_contains_word_in_file("positive_adjectives.txt", raw_msg):
                    await message.reply("{} {} on my shi".format(wf.get_random_line_in_file("positive_adjectives.txt"), wf.get_random_line_in_file("nouns.txt")))
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
            bot_test_channel = discord.Client.get_channel(client, bot_test_channel_id)
            await bot_test_channel.send("check_reations crashed: \n " + traceback.format_exc())


async def create_poll_message():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    channel = discord.Client.get_channel(client, schedule_channel_id)
    now = datetime.datetime.now()
    day = now + datetime.timedelta(days=7)
    await channel.send("Poll for **{}**  {}".format(days[int(day.weekday())], str(day.date())))


async def wait_for_poll():
    while True:
        try: 
            now = datetime.datetime.now()
            if now.hour == 19 and now.minute== 0 and now.second == 0:
                await create_poll_message()
                await asyncio.sleep(1)
            await asyncio.sleep(0.5)
        except Exception:
            print(traceback.format_exc())
            bot_test_channel = discord.Client.get_channel(client, bot_test_channel_id)
            await bot_test_channel.send("check_reations crashed: \n " + traceback.format_exc())

async def wait_for_reboot():
    while True:
        try: 
            now = datetime.datetime.now()
            if now.hour == 7 and now.minute== 0 and now.second == 0:
                reboot_system()
        except Exception:
            print(traceback.format_exc())
            bot_test_channel = discord.Client.get_channel(client, bot_test_channel_id)
            await bot_test_channel.send("check_reations crashed: \n " + traceback.format_exc())

def reboot_system():
    print("Rebooting system.")
    os.system("sudo reboot")

cur_dir = pathlib.Path(__file__).parent.resolve()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

with open(os.path.join(cur_dir, "botkey.txt"), "r") as f:
    botkey = f.readline()

#client.loop.create_task(wait_for_poll())
client.run(botkey)
