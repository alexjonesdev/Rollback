#---==IMPORTS==---

#---==CLASSES==---
class Player:
    def __init__(self, number = 0):
        self.number = number

class PlayerGenerator:
    def __init__(self):
        self.players = []

    def add_player(self, player = None):
        if player is None:
            self.players.append(Player(number = len(self.players) + 1))
        else:
            self.players.append(player)