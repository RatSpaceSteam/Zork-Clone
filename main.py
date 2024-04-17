import random

class Player:
  
  def __init__(self):
    self.location = [4,0]
    self.inventory = []
    self.command_list = ["List of commands:", "", "Movement:", "Up", "Down", "Left", "Right", "", "Items:", "Take", "Use", "Drop", "I/Inv/Inventory", "", "Other:", "Loc/Location", "Help"]

  def printInventory(self):
    print(self.inventory)

  def takeItem(self):
    if world[self.location[0]][self.location[1]] == "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement." or world[self.location[0]][self.location[1]] == "There is nothing here other than a grotesque wound in the universe from which you can hear inhuman weeping." or world[self.location[0]][self.location[1]] == "Here stands a tree that looks a mile high. Looking at it you feel a sense of overwhelming fear." or world[self.location[0]][self.location[1]] == "There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future.":
      print("There is nothing of use here.")
    elif world[self.location[0]][self.location[1]] == "Here there seems to be a set of armor. It emits bright colors that don't exist in the visible light spectrum, and staring at it for too long seems to anger it.":
      print("As you reach out and pick up the set of armor, it glows brighter in even more impossible colors. As you stow it in your bag, you feel a rush of happiness, euphoria, and hope. For some odd reason, you cry a little.")
      self.inventory.append("Impossible armor")
      world[0][0] = "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement."
    elif world[self.location[0]][self.location[1]] == "There is a sword on the ground. It seems to be fashioned for individuals with only 3 fingers on each hand. It also seems to be glowing in multiple colors at once, you feel slightly dizzy.":
      print("As you pick up the sword, adapting to its strange grip, the blue color of it seems to amplify a lot. As you stow it in your pack, you hear a thought in your head that you didn't make. It reaches out it reaches out it reaches out. It reaches out, 113 times a second, it reaches out.")
      self.inventory.append("Odd gripped, mad sword")
      world[1][1] = "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement."
    elif world[self.location[0]][self.location[1]] == "A rock. That's it? A !^%@#*& rock!? Oh well, it doesn't seem to be too weird other than that it's bleeding.":
      print("Despite your better reasoning, you feel the need to reach out and take the utterly useless rock. It's wound closes rapidly, and you hear it trill a little as you stow it in your bag.")
      self.inventory.append("Living rock")
      world[3][0] = "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement."
    elif world[self.location[0]][self.location[1]] == "Here seems to be a key. It's made of an unknown material. It has a manufacturer called Mao-Kwikowski Mercantile, which has an established date several centuries into the future." and world[3][3] != "You look and see the most horrific creature in the universe. It seems to be a human, but wrong. Its proportions are all wrong, it has a head 50% larger than its torso, and its skin is gray as well as glowing blue in some parts. It sets its sights on you, it doesn't look happy.":
      print("You take the key. It feels like it's made of pure light, how strange. The Mao-Kwik logo on it seems to wink at you and then shuts off of the mini-display.")
      self.inventory.append("Mao-Kwikowski key")
      world[4][3] = "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement."
    elif world[self.location[0]][self.location[1]] == "Here seems to be a key. It's made of an unknown material. It has a manufacturer called Mao-Kwikowski Mercantile, which has an established date several centuries into the future." and world[3][3] == "You look and see the most horrific creature in the universe. It seems to be a human, but wrong. Its proportions are all wrong, it has a head 50% larger than its torso, and its skin is gray as well as glowing blue in some parts. It sets its sights on you, it doesn't look happy.":
      print("Trying to take the key, you feel that it is the planck temperature. Somehow not immediately vaporizing into your constituent atoms, you retract your hand away at around 12% the speed of light. It seems the key does not want you to take ownership over it.")
    elif world[self.location[0]][self.location[1]] == "You look and see the most horrific creature in the universe. It seems to be a human, but wrong. Its proportions are all wrong, it has a head 50% larger than its torso, and its skin is gray as well as glowing blue in some parts. It sets its sights on you, it doesn't look happy.":
      print("There is nothing of use here, other than a quick death, if that's what you are looking for.")

  def useItem(self):
    if player_input.upper() == "USE ARMOR" and "Impossible armor" in self.inventory:
      print("As you fasten the armor onto your torso, you have a thought in your head that it means that no one can see you. Suddenly, it begins to glow your favorite color, it seems to comfort you.")
      self.inventory.remove("Impossible armor")
      return 1
    elif player_input.upper() == "USE ARMOR" and "Impossible armor" not in self.inventory:
      print("You don't have any armor in your bag.")
      return 1
    elif player_input.upper() == "USE SWORD" and "Odd gripped, mad sword" in self.inventory:
      if world[self.location[0]][self.location[1]] == "You look and see the most horrific creature in the universe. It seems to be a human, but wrong. Its proportions are all wrong, it has a head 50% larger than its torso, and its skin is gray as well as glowing blue in some parts. It sets its sights on you, it doesn't look happy.":
        if world[0][0] == "Here there seems to be a set of armor. It emits bright colors that don't exist in the visible light spectrum, and staring at it for too long seems to anger it." or world[0][0] == "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement." and "Impossible Armor" in self.inventory:
          chancetodefeat = random.randint(1,100)
          self.inventory.remove("Odd gripped, mad sword")
          if 75 >= chancetodefeat:
            print("You strike directly at where the monster's heart is supposed to be, it immediately freezes, screams a most horrific scream, and collapses onto the ground without so much as another sound. Down to the South, you hear a small boom.")
            world[3][3] = "Here lies the corpse of the slain monster. From time to time, it still glows and twitches, but it's just plain dead. It seems to excrete liquid oxygen from where you striked it."
            return 1
          else:
            print("You attempt to strike, but miss. With its deformed arm it grabs your face. It plants its massive nails into your head, and you begin to be infected and you can't stop the work you can't stop the work you can't stop the work because it reaches out it reaches out 113 times a second and won't let them rest.")
            print()
            print("GAME OVER")
            return 0
        elif world[0][0] == "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement." and "Impossible Armor" not in self.inventory:
          self.inventory.remove("Odd gripped, mad sword")
          print("You strike directly at where the monster's heart is supposed to be, it immediately freezes, screams a most horrific scream, and collapses onto the ground without so much as another sound. Down to the South, you hear a small boom.")
          world[3][3] = "Here lies the corpse of the slain monster. From time to time, it still glows and twitches, but it's just plain dead. It seems to excrete liquid oxygen from where you striked it."
          return 1
      else:
        print("There is nothing here that needs killing.")
        return 1
    elif player_input.upper() == "USE SWORD" and "Odd gripped, mad sword" not in self.inventory:
      print("You do not have any swords to spare.")
      return 1
    elif player_input.upper() == "USE ROCK" and "Living rock" in self.inventory:
      if world[self.location[0]][self.location[1]] == "You look and see the most horrific creature in the universe. It seems to be a human, but wrong. Its proportions are all wrong, it has a head 50% larger than its torso, and its skin is gray as well as glowing blue in some parts. It sets its sights on you, it doesn't look happy.":
        if world[0][0] == "Here there seems to be a set of armor. It emits bright colors that don't exist in the visible light spectrum, and staring at it for too long seems to anger it." or world[0][0] == "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement." and "Impossible Armor" in self.inventory:
          chancetodefeat = random.randint(1,100)
          if 25 >= chancetodefeat:
            print("You toss the wailing stone at the monster's head is, the force of the throw punctures straight through its deformed head, and it collapses onto the ground. As it falls and wails in pain, you hear a small boom to the South.")
            world[3][3] = "Here lies the corpse of the slain monster. From time to time, it still glows and twitches, but it's just plain dead. It seems to excrete liquid oxygen from it's head where you stoned it."
            return 1
          else:
            print("You throw the stone as hard as you can, but miss. With its deformed arm it grabs your face. It plants its massive nails into your head, and you begin to be infected and you can't stop the work you can't stop the work you can't stop the work because it reaches out it reaches out 113 times a second and won't let them rest.")
          print()
          print("GAME OVER")
          return 0
        elif world[0][0] == "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement." and "Impossible Armor" not in self.inventory:
          chancetodefeat = random.randint(1,100)
          if 50 >= chancetodefeat:
            print("You toss the wailing stone at the monster's head is, the force of the throw punctures straight through its deformed head, and it collapses onto the ground. As it falls and wails in pain, you hear a small boom to the South.")
          world[3][3] = "Here lies the corpse of the slain monster. From time to time, it still glows and twitches, but it's just plain dead. It seems to excrete liquid oxygen from it's head where you stoned it."
          return 1
        else:
          print("You throw the stone as hard as you can, but miss. With its deformed arm it grabs your face. It plants its massive nails into your head, and you begin to be infected and you can't stop the work you can't stop the work you can't stop the work because it reaches out it reaches out 113 times a second and won't let them rest.")
          print()
          print("GAME OVER")
          return 0
      else:
        print("There is nothing here that needs stoning.")
        return 1
    elif player_input.upper() == "USE ROCK" and "Living rock" not in self.inventory:
      print("You do not have any rocks to spare.")
      return 1
    elif player_input.upper()== "USE HANDS":
      if world[self.location[0]][self.location[1]] == "You look and see the most horrific creature in the universe. It seems to be a human, but wrong. Its proportions are all wrong, it has a head 50% larger than its torso, and its skin is gray as well as glowing blue in some parts. It sets its sights on you, it doesn't look happy.":
        if world[0][0] == "Here there seems to be a set of armor. It emits bright colors that don't exist in the visible light spectrum, and staring at it for too long seems to anger it." or world[0][0] == "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement." and "Impossible Armor" in self.inventory:
          print("You throw the hardest punch you can, but it feels like punching a wall made of lead. As you wail in pain, the creature looks down at you, seemingly amused. With its deformed arm it grabs your face. It plants its massive nails into your head, and you begin to be infected and you can't stop the work you can't stop the work you can't stop the work because it reaches out it reaches out 113 times a second and won't let them rest.")
          print()
          print("GAME OVER")
          return 0
        elif world[0][0] == "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement." and "Impossible Armor" not in self.inventory:
          chancetodefeat = random.randint(1,100)
          if 25 >= chancetodefeat:
            print("You quickly throw the hardest punch you can towards what you assume is one of the monster's weak spots. It is unaffected, but a small device starts blinking red where you hit it and wails an alarm. You jump out and away as the creature gets blown to pieces, and you hear a secondary small explosion to the south.")
            world[3][3] = "Here lies the remains of the exploded monster, its blue blood and symmetrical organs slowly dying. It's brain appears to be made of a single diamond."
            return 1
          else:
            print("You throw the hardest punch you can, but it feels like punching a wall made of lead. As you wail in pain, the creature looks down at you, seemingly amused. With its deformed arm it grabs your face. It plants its massive nails into your head, and you begin to be infected and you can't stop the work you can't stop the work you can't stop the work because it reaches out it reaches out 113 times a second and won't let them rest.")
            print()
            print("GAME OVER")
            return 0
    elif player_input.upper() == "USE KEY" and "Mao-Kwikowski key" in self.inventory:
      if world[self.location[0]][self.location[1]] == "It's a door. Cryptically, it reads: WARNING, MAGNETIC CONTAINMENT EXPLOSIVE DANGER in faded letters. The door appears to be locked.":
        print("Being ready for anything, you insert the key into the lock and the door, and turn it. Expecting immediate death and realizing that it hasn't come, you opened your eyes that you hadn't realized were clenched closed. It's whitespace beyond the door, endless white. You step in, and the door vanishes. You feel yourself being engulfed in energy, it doesn't appear to be harmful. With a doompf, you fall on your bed and see you are back home, it seems to be night. You look towards your ceiling, and see a wound in reality rapidly close. You sincerely hope that that is the last of whatever weirdness the universe, or beyond, has in store for you. You close your eyes, and fall into sweet dreams....")
        print("Thank you for playing my zork project!")
        return 0
      else:
        print("There are no keyholes in sight.")
    elif player_input.upper() == "USE KEY" and "Mao-Kwikowski key" not in self.inventory:
      print("You do not have any keys in your bag")
      
  def printLocation(self):
    print(self.location)

  def printCommandList(self):
    for i in range(len(self.command_list)):
      print(self.command_list[i])

  def move(self, player_input):
    if player_input.upper() == "UP":
        if 0 > self.location[0] - 1:
          print("Existence seems to deteriorate here. You don't know what lies beyond this area, but you aren't keen to find out.")
        elif self.location[0] - 1 == 3 and self.location[1] == 1:
          print("There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future. Feeling reasonably creeped out, you back away.")
        else:
          self.location[0] -= 1
          print(world[self.location[0]][self.location[1]])
    if player_input.upper() == "DOWN":
      if self.location[0] + 1 > 5:
        print("Existence seems to deteriorate here. You don't know what lies beyond this area, but you aren't keen to find out.")
      elif self.location[0] + 1 == 3 and self.location[1] == 1:
          print("There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future. Feeling reasonably creeped out, you back away.")
      elif self.location[0] + 1 == 4 and self.location[1] == 2:
          print("There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future. Feeling reasonably creeped out, you back away.")
      else:
        self.location[0] += 1
        print(world[self.location[0]][self.location[1]])
    if player_input.upper() == "LEFT":
      if 0 > self.location[1] - 1:
        print("Existence seems to deteriorate here. You don't know what lies beyond this area, but you aren't keen to find out.")
      elif self.location[1] - 1 == 1 and self.location[0] == 3:
          print("There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future. Feeling reasonably creeped out, you back away.")
      elif self.location[1] - 1 == 2 and self.location[0] == 4:
          print("There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future. Feeling reasonably creeped out, you back away.")
      else:
        self.location[1] -= 1
        print(world[self.location[0]][self.location[1]])
    if player_input.upper() == "RIGHT":
      if self.location[1] + 1 == 4:
        print("Existence seems to deteriorate here. You don't know what lies beyond this area, but you aren't keen to find out.")
      elif self.location[1] + 1 == 1 and self.location[0] == 3:
          print("There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future. Feeling reasonably creeped out, you back away.")
      elif self.location[1] + 1 == 2 and self.location[0] == 4:
          print("There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future. Feeling reasonably creeped out, you back away.")
      else:
        self.location[1] += 1
        print(world[self.location[0]][self.location[1]])
    
def shillCreatorName():
  one = ["C", "C", "C", "C", "C", "C", "C", "C", "C"]
  two = ["R", "R", "R", "R", "R", "R", "R", "R", "R"]
  three = ["E", "E", "E", "E", "E", "E", "E", "E", "E"]
  four = ["A", "A", "A", "A", "A", "A", "A", "A", "A"]
  five = ["T", "T", "T", "T", "T", "T", "T", "T", "T"]
  six = ["E", "E", "E", "E", "E", "E", "E", "E", "E"]
  seven = ["D", "D", "D", "D", "D", "D", "D", "D", "D"]
  
  eight = ["B", "B", "B", "B", "B", "B", "B", "B", "B"]
  nine = ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"]
  
  ten = ["J", "J", "J", "J", "J", "J", "J", "J", "J"]
  eleven = ["A", "A", "A", "A", "A", "A", "A", "A", "A"]
  twelve = ["C", "C", "C", "C", "C", "C", "C", "C", "C"]
  thirteen = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
  fourteen = ["B", "B", "B", "B", "B", "B", "B", "B", "B"]
  
  fifteen = ["P", "P", "P", "P", "P", "P", "P", "P", "P"]
  sixteen = ["A", "A", "A", "A", "A", "A", "A", "A", "A"]
  seventeen = ["T", "T", "T", "T", "T", "T", "T", "T", "T"]
  eighteen = ["T", "T", "T", "T", "T", "T", "T", "T", "T"]
  
  for a in range(len(one)):
    print(one[a])
  print()
  for b in range(len(two)):
    print(two[b])
  print()
  for c in range(len(three)):
    print(three[c])
  print()
  for d in range(len(four)):
    print(four[d])
  print()
  for e in range(len(five)):
    print(five[e])
  print()
  for f in range(len(six)):
    print(six[f])
  print()
  for g in range(len(seven)):
    print(seven[g])
  print()
  for h in range(len(eight)):
    print(eight[h])
  print()
  for i in range(len(nine)):
    print(nine[i])
  print()
  for j in range(len(ten)):
    print(ten[j])
  print()
  for k in range(len(eleven)):
    print(eleven[k])
  print()
  for l in range(len(twelve)):
    print(twelve[l])
  print()
  for m in range(len(thirteen)):
    print(thirteen[m])
  print()
  for n in range(len(fourteen)):
    print(fourteen[n])
  print()
  for o in range(len(fifteen)):
    print(fifteen[o])
  print()
  for p in range(len(sixteen)):
    print(sixteen[p])
  print()
  for q in range(len(seventeen)):
    print(seventeen[q])
  print()
  for r in range(len(eighteen)):
    print(eighteen[r])
  return 0
  
world = [["Here there seems to be a set of armor. It emits bright colors that don't exist in the visible light spectrum, and staring at it for too long seems to anger it.", "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement.", "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement.", "It's a door. Cryptically, it reads: WARNING, MAGNETIC CONTAINMENT EXPLOSIVE DANGER in faded letters. The door appears to be locked."],
  ["The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement.", "There is a sword on the ground. It seems to be fashioned for individuals with only 3 fingers on each hand. It also seems to be glowing in multiple colors at once, you feel slightly dizzy.", "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement.", "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement."],
  ["The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement.", "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement.", "Here stands a tree that looks a mile high. Looking at it you feel a sense of overwhelming fear.", "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement."],
  ["A rock. That's it? A !^%@#*& rock!? Oh well, it doesn't seem to be too weird other than that it's bleeding.", "There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future.", "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement.", "You look and see the most horrific creature in the universe. It seems to be a human, but wrong. Its proportions are all wrong, it has a head 50% larger than its torso, and its skin is gray as well as glowing blue in some parts. It sets its sights on you, it doesn't look happy."],
  ["You open your eyes. Everything around you seems wrong, you don't remember how you got here, and you don't plan on staying.", "The ground here seems to be made of wailing cement. Nothing of interest seems to be here other than the wailing souls of the individuals packed into the cement.", "There is a wall here that seems to replicate your bedroom. On it is scribed the exact time and date of what you realize is your birth, following that is the exact time and date of an unspecified event scant few minutes into your future.", "Here seems to be a key. It's made of an unknown material. It has a manufacturer called Mao-Kwikowski Mercantile, which has an established date several centuries into the future."]]

WRobinnet = Player()
gameRunning = 1
print(world[4][0])
world[4][0] = "There is nothing here other than a grotesque wound in the universe from which you can hear inhuman weeping."
while gameRunning == 1:
  print()
  player_input = input("What would ye like to doeth next?: ")
  if player_input.upper() == "UP" or player_input.upper() == "DOWN" or player_input.upper() == "LEFT" or player_input.upper() == "RIGHT":
    print()
    WRobinnet.move(player_input)
  elif player_input.upper() == "INVENTORY" or player_input.upper() == "I" or player_input.upper() == "INV":
    print()
    WRobinnet.printInventory()
  elif player_input.upper() == "LOCATION" or player_input.upper() == "LOC":
    print()
    WRobinnet.printLocation()
  elif player_input.upper() == "HELP":
    print()
    WRobinnet.printCommandList()
  elif player_input.upper() == "TAKE":
    print()
    WRobinnet.takeItem()
  elif player_input.upper() == "USE ARMOR" or player_input.upper() == "USE SWORD" or player_input.upper() == "USE ROCK" or player_input.upper() == "USE KEY" or player_input.upper() == "USE HANDS":
    print()
    gameRunning = WRobinnet.useItem()
  elif player_input.upper() == "SHILL":
    gameRunning = shillCreatorName()
  else:
    print()
    print("I don't know what '" + player_input + "' means.")