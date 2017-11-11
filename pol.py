import discord
import asyncio
import datetime


class Listener(discord.Client):
    async def on_ready(self):
        for server in self.servers:
            print('Detecting thoughtcrime on server %s' % server.name)

    async def on_message(self, message):
        print('%s/%s#%s->%s | %s' % (message.timestamp, message.server.name, message.channel.name, message.author.name, message.content))


if __name__ == '__main__':
    with open('tokens.txt') as f:
        tokens = [token for token in f.read().split('\n') if token]

    listener = Listener()
    listener.run(tokens[0])
