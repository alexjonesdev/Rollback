#---==IMPORTS==---
import random

#---==CLASSES==---
class Player:
    """The base player class."""
    def __init__(self, number = 0):
        self.number = number

class Bot(Player):
    """A non-playable player with automated functionality."""
    def get_input(self):
        """Randomly generates an input"""
        pass

#---==MAIN LOGIC==---


#-------------------------------------------------------
# class PlayerGenerator:
#     instance = None
#     class __PlayerGenerator:
#         def __init__(self, players = []):
#             self.players = players

#     def __init__(self, players):
#         if not PlayerGenerator.instance:
#             PlayerGenerator.instance = PlayerGenerator.__PlayerGenerator(players)
#         else:
#             PlayerGenerator.instance.players = players

#     def add_player(self, player = None):
#         if player is None:
#             self.players.append(Player(number = len(self.players) + 1))
#         else:
#             self.players.append(player)