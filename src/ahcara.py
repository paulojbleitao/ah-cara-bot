import discord
from random import randint

class AhCara(discord.Client):
    async def on_ready(self):
        self.count = 0
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if 'ah cara' in message.content and not message.author.bot:
            self.count += 1
            zeroes = randint(1, 4)
            number = randint(1, 10**zeroes)
            await message.channel.send(f'momiento ah cara número {randint(1, number)}')
        elif message.content == '!ahcara':
            await message.channel.send(f'já tivemos {self.count} momientos ah cara')
