#BECOME A POKEMON MASTER

#classes

class Pokemon():
  def __init__(self, name, type, level=5, max_health=5):
    self.name = name
    self.level = level
    self.type = type
    self.health = 5 * level
    self.max_health = 5 * level
    self.is_knocked_out = False

#the code below will give you its name, and the player's health
        
  def __repr__(self):
    return self.name
        

#Giving the pokemon class some functionality

  def knock_out (self):
        self.is_knocked_out = True
        print ("{name} has been Knocked Out".format(name = self.name))
        if self.health !=0:
            self.health = 0
            print("{name} has been knocked out!".format(name = self.name))

#Method to Revive a pokemon

  def revive(self):
        self.is_knocked_out = False
        if self.health == 0:
            self.health = 1
            print ("{name} has now been Revived!!".format(name = self.name))
   
#takes health from pokemon
  def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.knock_out()
            print ("{name} now has {health} health.".format(name = self.name, health = self.health))
            
#adds health to pokemon
  def gain_health(self, helth):
        self.health += health
        if self.health >= max_health:
            self.health = self.max_health
        if self.is_knocked_out:
            self.revive()
        else:
            print("{name} now has {health} health.".format(name = self.name, health = self.health))
            
#attack method
  def attack(self, other_pokemon):
        # Checks to make sure the pokemon isn't knocked out
        if self.is_knocked_out:
            print("{name} can't attack because it is knocked out!".format(name = self.name))
            return
        # If the pokemon attacking has a disadvantage, then it deals damage equal to half its level to the other pokemon
        if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = round(self.level * 0.5)))
            print("It's not very effective")
            other_pokemon.lose_health(round(self.level * 0.5))
        # If the pokemon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other pokemon
        if (self.type == other_pokemon.type):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
            other_pokemon.lose_health(self.level)
        # If the pokemon attacking has advantage, then it deals damage equal to double its level to the other pokemon
        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
            print("It's super effective")
            other_pokemon.lose_health(self.level * 2)


      
#three classes that are sub class to pokemon
class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)

#creating a Trainer class
class Trainer:
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name      
        
#method to print the name of the trainer, the pokemon they currently have
    def __repr__(self):
       print("The trainer {name} has the following pokemon".format(name = self.name))
       for pokemon in self.pokemons:
           print(pokemon)
       return "The current active pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)
           

#Giving the trainer some functionality


    def use_potion(self):
        # Uses a potion on the active pokemon, assuming you have at least one potion.
        if self.potions > 0:
            print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
            # A potion restores 20 health
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You have no portions left!!")
            
    def attack_other_trainer(self, other_trainer):
        # Your current pokemon attacks the other trainer's current pokemon
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)
        


a = Charmander(7)
b = Squirtle()
c = Squirtle(1)
d = Bulbasaur(10)
e = Charmander()
f = Squirtle(2)

#lets test it, shall we :)
trainer_one = Trainer([d,b,a], 4, input("enter trainer name "))
trainer_two = Trainer([c,e,f], 5, input("enter trainer name "))

print(trainer_one)
print(trainer_two)


