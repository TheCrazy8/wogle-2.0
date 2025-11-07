import datetime
import random
try: 
  from colored import Fore, Back, Style
except Exception:
  Fore = None
  Back = None
  Style = None
  print("could not install colored, text will be default")

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
      # enemy turn
      if enemy.turn():
        self.health -= enemy.damage
      # player turn
      action = input("Choose your action (attack/heal/quit): ").strip().lower()
      if action == "attack":
        damage = random.randint(5, 15)
        enemy.health -= damage
        print(f"{Fore.green}You attacked the enemy! Dealt {damage} damage!{Style.reset}")
        self.score += damage
        if enemy.health <= 0:
          print(f"{Fore.blue}Enemy defeated! You win!{Style.reset}")
      elif action == "heal":
        heal_amount = random.randint(10, 20)
        self.health += heal_amount
        print(f"{Fore.green}You healed yourself for {heal_amount} health!{Style.reset}")
      elif action == "quit":
        print("You quit the game.")
        self.is_over = True
      else:
        print("Invalid action. Please choose attack, heal, or quit.")
      # check player health
      if self.health <= 0:
        print(f"{Fore.red}You have been defeated! Game over.{Style.reset}")
        self.is_over = True
      
      if enemy.health <= 0:
        print(f"{Fore.blue}Enemy defeated! You win!{Style.reset}")
        enemy.initialhealth += enemy.initialhealth // 2
        enemy.health = enemy.initialhealth
        self.level += 1
        print(f"Level up! You are now on level {self.level}.")

class enemy:
  def __init__(self):
    self.damage = 10
    self.initialhealth = 50
    self.health = 50

  def turn(self):
    if self.health > self.initialhealth * 0.3:
      attack_chance = 0.7
    else:
      attack_chance = 0.4
    if random.random() < attack_chance:
      print(f"{Fore.red}Enemy Attacked! Dealt {self.damage} damage!{Style.reset}")
      return True
    return False

enemy = enemy()
game = game()

game.__init__()
