import random

# creating classes for the pokemon with different stats
class pokemon:
    def __init__(self, name, health, strength, defence):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence

    # defining attack function and the 4 attacks the player can make its pokemon do
    def attack(player, opponent):
        choice = input(
            "\nWhat move would you like to make? \n Leach seed, \n scratch, \n quick attack, \n howl\n").lower()
        if choice == "leach seed":
            # leaches 10% of the opponents health
            leached_health = opponent.health / 10
            opponent.health = opponent.health - leached_health
            party[current_pokemon].health = party[current_pokemon].health + leached_health
            print("Your health is now :.", party[current_pokemon].health)
        elif choice == "scratch" or choice == "quick attack":
            damage = ((party[current_pokemon].strength * actions[choice] * opponent.defence) / 10)
            print("You deal:.", damage, " damage")
            opponent.health = opponent.health - damage
        elif choice == "howl":
            party[current_pokemon].strength = party[current_pokemon].strength + (actions[choice])
            print('You increase your strength')
        else:
            print("Not a valid move, try again!")

    def CPU_attack(player, opponent):
        CPU_choice = random.choice(list(actions))
        if CPU_choice == "leach seed":
            leached_health = party[current_pokemon].health / 10
            party[current_pokemon].health = party[current_pokemon].health - leached_health
            opponent.health = opponent.health + leached_health
            print("The opponent heals its health to :.", opponent.health)
        elif CPU_choice == "scratch" or CPU_choice == "quick attack":
            damage = ((opponent.strength * actions[CPU_choice] * party[current_pokemon].defence) / 100)
            print("Your opponent uses", CPU_choice, " and deals:.", damage, " damage")
            party[current_pokemon].health = party[current_pokemon].health - damage
        elif CPU_choice == "howl":
            opponent.strength = opponent.strength + (actions[CPU_choice])
            print('The opponent increases his strength')


# players pokemon
pikachu = pokemon('Pikachu', 100, 10, 10)
charmander = pokemon('Charmander', 100, 12, 8)
squirtle = pokemon('Squirtle', 100, 8, 12)
bulbasaur = pokemon('Bulbasaur', 120, 10, 10)
mewtwo = pokemon('Mewtwo', 300, 20, 20,)

# opponent pokemon
o_pikachu = pokemon('Pikachu', 100, 10, 10)
o_charmander = pokemon('Charmander', 100, 12, 8)
o_squirtle = pokemon('Squirtle', 100, 8, 12)
o_bulbasaur = pokemon('Bulbasaur', 120, 10, 10)
o_mewtwo = pokemon('Mewtwo', 300, 20, 20, )

# define the players party as a list
party = []

# the list the player takes from to add pokemon to his party
unused_pokemon = [pikachu, charmander, squirtle, bulbasaur]

# list used for opponent pokemon battles during
global o_pokemon_party
o_pokemon_party = [o_charmander, o_squirtle, o_bulbasaur]

# current pookemon is an integer used to repersent the current pokemon from the party list
current_pokemon = 0

global victory
global game_over
game_over = False

# the moves that the pokemon can make
actions = {'scratch': random.randrange(10, 20),
           'leach seed': 0,
           'quick attack': random.randrange(20, 30),
           'howl': 5, }


# choosing first pokemon after meeting the professor
def pokemon_select():
    print('Choose your starter pokemon (A< B C or D):')
    print('A: Pikachu')
    print('B: Charmander')
    print('C: Squirtle')
    print('D: Bulbasaur')

    while True:
        player_choice = input().upper()
        if player_choice == "A":
            chosen_pokemon = pikachu
            break
        elif player_choice == "B":
            chosen_pokemon = charmander
            break
        elif player_choice == "C":
            chosen_pokemon = squirtle
            break
        elif player_choice == "D":
            chosen_pokemon = bulbasaur
            break
        else:
            print("Invalid input! Try again.")
    party.append(chosen_pokemon)
    print('\nyou have chosen:', party[0].name)


# after defeating the opponent they can choose to add that pokemon to their party
def party_addition():
    party_addition = input('do you want to add the defeated pokemon to your party? (y/n)'.lower(), )
    if party_addition == 'y':
        party.append(unused_pokemon[0])
        del unused_pokemon[0]
        print('your party now consists of:', party)
    else:
        print('you continue on your journey')

# battle function
def battle():
    while (party[current_pokemon].health > 0 and opponent.health > 0):
        if party[current_pokemon].health > 0:
            party[current_pokemon].attack(opponent)
            print('\nOpponents ', opponent.name, 'health is now:', opponent.health)
        if opponent.health > 0:
            opponent.CPU_attack(party[current_pokemon])
            print("Your ", party[current_pokemon].name, "'s health is now: ", party[current_pokemon].health)
        if party[current_pokemon].health <= 0:
                break
        elif opponent.health <= 0:
            print('Congratulations you won!')
            victory = 'y'
            party_addition()
            break
    if party[current_pokemon].health <= 0:
        del party[current_pokemon]
        battle()
    elif party == []:
        game_over = True


def random_chance_encounter():
    r_chance = random.randrange(0, 100)
    if r_chance == (37 or 38 or 6 or 18):
        global chance_encounter
        chance_encounter == True
        party = [mewtwo]


# temporary battle function to test outline by simple y/n input from user if they win or not
'''def battle():
    global victory
    victory = input ('do you win or not (y/n)')
    while not victory == 'y':
        if  (victory == 'y'):
            print('Congratulations, you won!')
            break
        else:
            print('Try again')
            victory = input ('do you win or not (y/n)')'''

victory_count = 0
# introduction opening

if game_over == False:
    print(''' Hello to the world of pokemon, you will soon embark on an adventure to 
become the champion of this region, to do this you must first defeat 3 
challengers to be able to fight the chamption, after you defeat him you 
will then be the champion''')

    pokemon_select()
    print('\nGreat!')
    print("Lets have a battle here against my Pikachu!")
    opponent = (o_pikachu)
    while party[current_pokemon].health >= 0 and opponent.health > 0:

        party[current_pokemon].attack(opponent)
        print('Opponents ', opponent.name, 'health is now:', opponent.health)

        opponent.CPU_attack(party[current_pokemon])
        print(party[current_pokemon].name, "'s health is now: ", party[current_pokemon].health)
        if party[current_pokemon].health <= 0:
            print('Thats s shame looks like you arent good enough to start your journey maybe some other time.')
            victory ='n'
            game_over = True
            break
        elif opponent.health <= 0:
            print('congratulations you won!')
            victory = 'y'
            break
else:
    game_over = True
    print("Game Over")


""" Getting 3 victories"""
if game_over == False:
    victory_count = 0
    while not victory_count == 3:
        #assigns the first opponent pokemon in o_pokemon_party 
        opponent = o_pokemon_party[0]
        print('on your journey you come across a challenger who challenges you with', opponent.name)
        battle()
        if party == []:
            break
        if (victory == 'y'):
            victory_count = victory_count + 1
            #deletes the first pokemon in o_pokemon_party so the next one is now 0 
            del o_pokemon_party[0]
            print('you have: ', victory_count, ' victories')    

else:
    print('')
""" challenging champion"""

if game_over == False and victory_count == 3:
    print('\nYou now have enough victories to challenge the champion and his Mewtwo, and he accepts your challenge')
    opponent = o_mewtwo
    battle()
    while not victory == 'n':
        if (victory == 'y'):
            print('\nCongratulations you have defeated the chapmpion and become the champion')
            break
        else:
            print('Ha your going to have to do much better than that do defeat me')
            print('THE END')

else:
    print('')
