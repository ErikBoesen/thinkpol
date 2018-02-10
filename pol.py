import discord
import asyncio
import datetime
import argparse


class Listener(discord.Client):
    async def on_ready(self):
        print('-- Surveillance started --')
        for server in self.servers:
            print('Detecting thoughtcrime on server %s' % server.name)

    async def on_message(self, message):
        print('%s/%s#%s->%s | %s' % (message.timestamp, message.server.name if message.server else 'DM', message.channel.name, message.author.name, message.content))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('token')
    args = parser.parse_args()

    listener = Listener()
    listener.run(args.token)
