import discord
import datetime
import argparse


class Listener(discord.Client):
    async def on_ready(self):
        print('-- Surveillance started --')
        for server in self.servers:
            print('Detecting thoughtcrime on server %s' % server.name)

    async def on_message(self, msg):
        print('%s/%s#%s->%s | %s' % (msg.timestamp,
                                     msg.server.name if msg.server else 'DM',
                                     msg.channel.name,
                                     msg.author.name,
                                     msg.content))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('token')
    args = parser.parse_args()

    Listener().run(args.token)
