import handler
import random

patterns = ['!roll', '!Roll', '!ROLL']

class monobattleRoller(handler.Handler):
    
    def can_handle(self, message):
        if message.content.lower() in patterns:
            return True

    async def handle(self, message, client, collection, cache):
        li = []
        protoss_li = ['zealot','stalker','adept','sentry','immortal','colossus','disrupter','pheonix','voidray','oracle','tempest','high templar','dark templar','archon']
        roll = random.randint(1,14)
        roll -= 1
        li.append(protoss_li[roll])
        roll2 = random.randint(1,15)
        roll2 -= 1
        terran_li = ['marine','marauder','reaper','ghost','widowmine','hellion','tank','cyclone','thor','viking','liberator','raven','banshee','cattlebruiser','hellbat']
        li.append(terran_li[roll2])
        zerg_li = ['zergling','baneling','roach','ravager','muta','corrupter','hydra','lurker','infestor','swarmhost','viper','ultra','broodlord','queens']
        roll3 = random.randint(1,14)
        roll3 -= 1
        li.append(zerg_li[roll3])
        msg = "Protoss: " + li[0] + "\nZerg: " + li[2] + "\nTerran: " + li[1]
        await message.channel.send(msg)

