class creature:
    def __init__ (self, name, health, strength, defence, accuracy):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.accuracy = accuracy 
 
def creature_select():
    pikachu = creature('Pikachu', 100, 10, 10, 10)
    charmander = creature('Charmander', 100, 12, 8, 10)
    squirtle = creature('Squirtle', 100, 8, 12, 10)
    bulbasaur = creature('Bulbasaur', 120, 10, 10, 8)
    eevee = creature('Eevee', 80, 10, 10, 12)
    my_creature = [pikachu, charmander, squirtle, bulbasaur, eevee]
    player_creature = input("select a character" + my_creature)

def main():
    player_creature
    print ('You have chosen:' + player_creature)

my_creature
    
    