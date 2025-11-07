import datetime
import random
try: 
  from colored import Fore, Back, Style
except Exception:
  Fore = None
  Back = None
  Style = None
  print("could not install colored text, will be default")

class game:
  def __init__(self):
    self.start_time = datetime.datetime.now()
    self.score = 0
    self.level = 1
    self.is_over = False
    self.health = 100
    self.ticks = 0
    self.start()
    enemy.__init__()

  def start(self):
    print("Game started!")
    self.play()

  def play(self):
    while not self.is_over == True:
      self.ticks += 1
      if enemy.attack():
        self.health -= enemy.damage

class enemy:
  def __init__(self):
    self.damage = 10

enemy = enemy()
game = game()

game.__init__()
