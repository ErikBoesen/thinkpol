# thinkpol
Proof-of-concept script for spying through compromised Discord bots.

**Logging into a bot without permission is a violation of Discord's TOS.**

## Usage
Run `pol.py` as you would any other Python program. Provide as the first argument the token of your target bot.

Example:
```sh
python3 pol.py MjySFFBbFt15U/ZPAxHhIT9TJcJ9VxOx.FrXNuQOj.aPNPUfRGHAHruv1EAuO21zY5mg3Rt3Fw
```
(No, that's not a real token.)

The script will output logs which can be read as Markdown. If you wish, you may redirect this output to a file:
```sh
python3 pol.py ... > ~/discord_log.md
```

# Licensing
This code is available under the [MIT License](LICENSE).
