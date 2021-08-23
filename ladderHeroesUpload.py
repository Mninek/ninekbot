import handler

patterns = ['!addladder', '!ADDLADDER', '!Addladder', '!addLadder']

class ladderHeroesUpload(handler.Handler):

    def can_handle(self, message):
        for pattern in patterns:
            if message.content.startswith(pattern):
                return True   

        return False

    async def handle(self, message, client, collection):
        params = message.content.split(' ')
        if len(params) != 3:
            await message.channel.send("Wrong format, to add your profile please do something like \"!addladder https://www.nephest.com/sc2/?type=character&id=85067&m=1#player-stats-summary\" ninek. Make sure to include your username as well")
        if not params[1].startswith("https://"):
            await message.channel.send("Please make sure the url starts with \"https://\" because ninek is too lazy to deal with that.")
        else:
            try:
                self.url = params[1]
                id = params[1][47:]
                id = id.split('&')
                id = id[0]
                self.id = id
                self.name = params[2]

                data = {'url': self.url,
                        'neph_id': id,
                        'name': self.name}

                rec_id = collection.insert_one(data)
            except:
                await message.channel.send("Something went wrong, Call ninek")
            await message.channel.send("You're in the database :+1:")

            await message.channel.send("Please make sure the url starts with \"https://\" because ninek is too lazy to deal with that.")