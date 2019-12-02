# CSCA20
CSCA20 Project
CSCA20
CSCA20 Project CSCA20 Project Report: Fall 2019

Team Member A
-
First Name: Muhammad Daniyal Last Name:Jafar Student Number:1003190691 UofT E-mail Address: daniyal.jafar@mail.utoronto.ca

Team Member B
-
First Name: Joshua Last Name: Dent Student Number: 1005989780 UofT E-mail Address: joshua.dent@mail.utoronto.ca

Project Plan
-
Project Title: Turn based Battle game

Provide a one paragraph description of your project

: The project is a text turn based game similar to Pokemon where the user picks one of 2 or more initial characters each with different attributes (strength, defence, health etc.) they then fight by choosing one of 4 attacks which will be 2 attacks (one high damage attack low accuracy, and one low damage high accuracy) one increases strength, one increases strength, one decreases the opponent's strength and one decreases their defence. The damage done will be randomly chosen from a range. The different character will have 4 of the 6 above attacks. After the character defeats the opponent they will have the option to add it to their party. Then they will encounter another character and fight them. The user will encounter up to 4 or 5 opponents in increasing difficulty, and if they defeat all of them they will have won. There is a random encounter where the character has the option to skip to the final boss.

Advice from TA: look up how to do objects - will make doing the characters better

What will you have done before you arrive at your tutorial next week? Will have finished the program with minimal bugs

What will you have done before you leave your tutorial next week?

What is your backup plan if things don’t work out as planned? The users character will be the only character the user can control and will “level up” as the user progresses through the game The chance encounter to skip to the final boss may not exist given time etc. Limit the number of characters/attacks the user can choose from/the game has.

Weekly Reports
-
Week 1: the majority of the lab was used to find partners and researching potential projects we could do and evaluating its ambition and coming up with a Pokemon style text based battle simulator. As well as planning out the outline of how the game was going to be played.

Week 2: we had planned to have the battle system and pokemon made with classes done by the first tutorial on november 19th 2-19, but due to other coursework not enough time was available for both partners to get much done except creation of the class pokemon, and 4 Pokemon were made. The lab was spent researching how we would plan the game to play out as suggested by the TA. the outline of the game consists of an introduction where the user chooses their starter Pokémon and then battles the professor’s pikachu until they win. After they must get 3 wins by fighting the 3 other starter Pokemon to add them to their party, in order to challenge the pokemon champion and win in order to become the champion. During the lab we also decided to use a function battle() that programs the battle sequence and adapted it to our project where needed such as changing variable names. Also we decided to limit the moves/actions/attacks of the pokemon to 4 that are shared across all of them but each Pokemon still has different attributes such as health strength and defence. After the lab we each worked on the party management system and battle system and are implementing the functions into the outline where needed and testing.

Final week report

Mostly everything that we set out to do was accomplished with the exception of a few given bugs such as Leach seed for the opponent not working After adding a pokemon to the party the pokemons names were not printed properly The opponents pokemon health got mixed up with the players pokemon health occasionally

References
-
https://codereview.stackexchange.com/questions/100852/pok%C3%A9mon-style-battle-game Used the attack() and battle() functions and changed the names to actual Pokemon attack moves and added a modifier (defence) to the calculation that changes the damage done depending on the player’s Pokemon's defence stat. And changed the heal option to the Pokemon move leech seed which steals the health from the opponent Pokemon and uses it to heal the players pokemon. The battle() function was taken and had variables changed to match the projects variables.

Final report: The battle function taken from the above hyperlink was discarded and remade from scratch due to bugs.

Repo & Video
-
Video: https://www.youtube.com/watch?v=ET5VRcT8A88&feature=youtu.be

Github repository:https://github.com/DanDLion210/CSCA20

How to run the program
-
download Game.py and Just press the run button
