import discord # type: ignore
import insultgen
import quotegen
import bullshit
import asyncio
import directedcomments as dc 
import reddit_scrape
import gpt
import traceback
import datetime

swearwords = ["fuck", "shit", "cunt", "dick", "cum", "piss", "ass", "hell", "cock", "slut", "prick", "bitch", ]
compliment_comments = []

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        raw_msg = message.content.lower()
        
        if message.author == client.user:
            return
        
        try: 

            if raw_msg.find("table") >= 0:
                await message.channel.send("┬─┬")

            for word in swearwords:
                if raw_msg.find(word) >= 0:
                    if bullshit.increase_bullshit_meter(message.author):
                        msg = insultgen.generate_insult(message.author)
                        channel = client.guilds[0].text_channels[0]
                        await channel.send(msg)
                    break
            
            if raw_msg.find("nut") >= 0:
                f = discord.File(open("elephant.png","rb"))
                await message.channel.send(file=f)

            if raw_msg.find("among") >= 0:
                await message.add_reaction("🤨")
        
            if raw_msg.find("sad") >= 0:
                await message.channel.send(quotegen.generate_quote())

            if raw_msg.find("willy") >= 0 or raw_msg.find(client.get_user(1228039945239924756).mention) >= 0: 
                if not dc.contains_positive_adjective(raw_msg):
                    await message.reply("the fuck you want?")
                    return

                if dc.negations_amount(raw_msg)%2==0:
                    await message.channel.send(gpt.get_compliment(raw_msg, message.author))
                else:
                    await message.channel.send(gpt.get_insult(raw_msg, message.author))
            
            if raw_msg.find("raise-error") >= 0:
                raise Exception

        except Exception: 
            print(traceback.format_exc())
            master = await client.fetch_user(226412002866757642)
            await message.channel.send(master.mention+" help i made a stinky")
            with open("logfile.txt", "w") as f:
                f.write(str(datetime.datetime.now())+"\n")
                f.write(traceback.format_exc())
            
            #TODO: make command to have the bot spit out the error message
            # as a dm maybe? 

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

with open("botkey.txt", "r") as f:
    botkey = f.readline()
client.run(botkey)