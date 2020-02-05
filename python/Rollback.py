#---==IMPORTS==---
import random, time, threading
from pynput import keyboard

#---==CONFIGURATION==---
update_fps = 300
render_fps = 2

#---==CLASSES==---
class Player:
    """The base player class."""
    def __init__(self, is_host, max_health = 1000, x = 0, y = 0):
        self.max_health = max_health
        self.health = max_health
        self.x = x
        self.y = y
        self.host = is_host

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def increase_health(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def __repr__(self):
        return "<Player: host=%s health=%d, x=%d, y=%d>" % (self.host, self.health, self.x, self.y)

class Bot(Player):
    """A non-playable player with automated functionality."""
    def __init__(self, is_host, max_health = 1000, x = 0, y = 0):
        super().__init__(is_host, max_health, x, y)

    def get_input(self):
        """Randomly generates an input."""
        return random.choice(['rock','paper','scissors'])

    def get_laggy_input(self):
        """Randomly generates an input including none."""
        return random.choice(['rock','paper','scissors', None])

class State:
    """Holds the current state of the game."""
    def __init__(self, players = []):
        self.players = players

class Game:
    """Keeps track of the game running"""
    running = True

#---==FUNCTIONS==---
def update():
    """Updates the game state based on the current inputs"""
    pass

def render(state):
    """Renders the current frame"""
    for player in state.players:
        print(player)

#Inputs
def on_press(key):
    """Captures keyboard key press."""
    # update()
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    """Captures keyboard key release."""
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        Game.running = False
        # Stop listener
        return False

#---==INITIALIZATION==---
#Start the game loop
# updater = threading.Thread(group=None, target=update, name='game_loop')

#Start the render loop
# renderer = threading.Thread(group=None, target=render, name='render_loop')

#Get inputs
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

#---==MAIN LOGIC==---
running = True
current_frame = 0
max_frames = 20
players = [Bot(True, 1000, 0, 0), Bot(False, 1000, 100, 0)]
frames = []

while current_frame <= max_frames:
    start = time.time()
    print('Player 1:', players[0].get_input(), 'Player 2:', players[1].get_input())
    # update()
    # render()
    current_frame += 1
    time.sleep(max(1./2 - (time.time() - start), 0))

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