import discord # type: ignore
import insultgen
import quotegen
import bullshit
import asyncio

swearwords = ["fuck", "shit", "cunt", "dick", "cum", "piss", "ass", "hell"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        raw_msg = message.content.lower()
        
        if message.author == client.user:
            return
        
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

        


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

with open("botkey.txt", "r") as f:
    botkey = f.readline()
client.run(botkey)