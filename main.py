import datetime
import random

class game:
  def __init__():
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
    while not self.is_over == true:
      self.ticks += 1
      if enemy.attack():
        self.health -= enemy.damage

class enemy:
  def __init__():
    self.damage = 10


game.__init__()
