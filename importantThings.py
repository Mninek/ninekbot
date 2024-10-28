import handler
import random

patterns = ['!bringoutthedancinglobsters']

class lobsters(handler.Handler):
    
    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection, cache):
        roll = random.uniform(0,1)
        msg = "Shh they're sleeping"
        if client.user.id == "995535732695379988":
            msg = "Go home Badger!"
        elif roll <= .1 or client.user.id == "314200471088922636":
            msg = "https://i.imgur.com/BMcur.gif"
        elif client.user.id == "995535732695379988":
            msg = "Go home Badger!"
        await message.channel.send(msg)

