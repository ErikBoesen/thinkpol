import discord
import datetime
import argparse
import sys


class Listener(discord.Client):
    async def on_ready(self):
        sys.stdout.write('Surveillance started!\n')
        sys.stdout.write('=====================\n')
        sys.stdout.write('**Logged in as %s#%s**  \n' % (self.user.name, self.user.discriminator))
        sys.stdout.write('Monitoring servers %s\n' % ', '.join(['`%s`' % server.name for server in self.servers]))
        sys.stdout.write('---------\n')
        sys.stdout.flush()

    async def on_message(self, msg):
        sys.stdout.write('- **%s/%s#%s->%s** ```%s```\n' % (msg.timestamp,
                                                            msg.server.name if msg.server else 'DM',
                                                            msg.channel.name,
                                                            msg.author.name,
                                                            msg.content))
        sys.stdout.flush()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('token')
    args = parser.parse_args()

    Listener().run(args.token)
