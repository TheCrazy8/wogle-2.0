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
      action = input("Choose your action (attack/heal/quit/use item): ").strip().lower()
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
      elif action == "use item":
        if items.current_items:
          print("Your items:", ", ".join(items.current_items))
          chosen_item = input("Which item do you want to use? ").strip()
          if chosen_item in items.current_items:
            if chosen_item == "Health Potion":
              heal_amount = 30
              self.health += heal_amount
              print(f"{Fore.green}You used a Health Potion and healed for {heal_amount} health!{Style.reset}")
              items.current_items.remove(chosen_item)
            else:
              print(f"{Fore.yellow}You used {chosen_item}, but nothing happened.{Style.reset}")
          else:
            print("You don't have that item.")
        else:
          print("You have no items to use.")
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

class items:
  def __init__(self):
    self.item_list = ["Health Potion", "Sword", "Shield"]
    self.current_items = []

  def add_item(self, item):
    if item in self.item_list:
      self.current_items.append(item)
      print(f"{Fore.yellow}You obtained a {item}!{Style.reset}")
    else:
      print("Item does not exist.")

  def remove_item(self, item):
    if item in self.current_items:
      self.current_items.remove(item)
      print(f"{Fore.yellow}You used a {item}.{Style.reset}")
    else:
      print("You don't have that item.")

  def list_items(self):
    return self.current_items

  def clear_items(self):
    self.current_items = []
    print("All items have been cleared.")

  def item_count(self):
    return len(self.current_items)

enemy = enemy()
game = game()
items = items()

game.__init__()
