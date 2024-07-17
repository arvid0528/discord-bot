import discord # type: ignore
import bullshit
import asyncio
import reddit_scrape
import gpt
import traceback
import datetime
import pathlib
import os
import random
import wordfiles as wf
import webscrape

swearwords = ["fuck", "shit", "cunt", "dick", "cum", "piss", "ass", "hell", "cock", "slut", "prick", "bitch", "sex", "nigga"]
compliment_comments = []

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        message.attachments

        raw_msg = message.content.lower()

        master_user = await client.fetch_user(226412002866757642)
        
        if message.author == client.user:
            return
        
        try: 

            if raw_msg.find("table") >= 0:
                await message.channel.send("┬─┬")

            for word in swearwords:
                if raw_msg.find(word) >= 0:
                    if bullshit.increase_bullshit_meter(message.author):
                        msg = wf.generate_insult(message.author)
                        channel = client.guilds[0].text_channels[0]
                        await message.channel.send(msg)
                    break
            
            if raw_msg.find("nut") >= 0:
                f = discord.File(open(os.path.join(cur_dir, "elephant.png"),"rb"))
                await message.channel.send(file=f)

            if raw_msg.find("among") >= 0:
                await message.add_reaction("🤨")
        
            if raw_msg.find("sad") >= 0:
                await message.channel.send(wf.generate_quote())

            if raw_msg.find("voice") >= 0:
                voice_state = message.author.voice
                if voice_state:
                    await voice_state.channel.connect()

            if raw_msg.find("willy") >= 0 or raw_msg.find(client.get_user(1228039945239924756).mention) >= 0: 
                if wf.sentence_contains_word_in_file("positive_adjectives.txt", raw_msg):
                    await message.reply("{} {}'s on my shi".format(wf.get_random_positive_adjective(), wf.get_random_noun()))
                elif wf.sentence_contains_word_in_file("negative_adjectives.txt", raw_msg):
                    await message.reply(wf.get_random_noun())
                else:
                    rand = random.randint(1, 10)
                    if rand <= 3:
                        await message.reply(wf.generate_quote())
                    elif rand <= 6:
                        await message.reply("{} {}".format(wf.get_random_positive_adjective(), wf.get_random_noun()))
                    elif rand <= 9:
                        await message.reply("{} {}".format(wf.get_random_negative_adjective(), wf.get_random_noun()))
                    else:
                        await message.channel.send(webscrape.get_random_wiki_page_first_sentence())


                """ if dc.negations_amount(raw_msg)%2==0:
                    await message.channel.send(gpt.get_compliment(raw_msg, message.author))
                else:
                    await message.channel.send(gpt.get_insult(raw_msg, message.author)) """
            
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

cur_dir = pathlib.Path(__file__).parent.resolve()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

with open(os.path.join(cur_dir, "botkey.txt"), "r") as f:
    botkey = f.readline()
client.run(botkey)