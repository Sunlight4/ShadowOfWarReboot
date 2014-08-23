import random
class Territory(object):
    def __init__(self, team, pos, adjacents):
        self.adjacents=adjacents
        self.pos=pos
        self.team=team
        names=["Tatooine", "Nabalis", "Dorma", "Erd", "Zook", "Shir", "Mordor",
               "Isengard", "World A", "World X", "Bubbleworld", "Dabranoid"]
        self.name=random.choice(names)
