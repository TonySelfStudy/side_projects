# Dungeons, Dragons, and 303 Beard Street! 
# Created 2020-04-13
# Last modified 2020-04-14

"""Create a desirable D&D Character to mount an attack on the most evil of Hickam Dungeon Masters!"""

from random import randint  # access random number generator function from python library

def print_header(str, char='*'):
    """Print header to seperate output
    str - text to print
    char - the charater repeated on next line for pizzaz"""
    print(f"{str}\n{char*len(str)}\n")

class DChar:
    """DChar stores all D & D Player Information"""

    # MIN_ROLL is the minimum value deemed acceptable for any DND_Character
    #          in the possible range of 3 to 18
    MIN_ROLL = 16
    # The D&D Character's innate qualities 
    QUALITIES = ['strength', 'dexterity', 'intelligence', 'wisdom', 'charisma', 'constitution']
    NUM_QUALITIES = len(QUALITIES) # Number of qualities for a single character


    def __init__(self, player_name):
        self.player_name = player_name
        self.characteristics={}
        self.set_characteristics() # initialize all to 0
        self.roll_character()
        self.display_character()

    def set_characteristics(self, rolls=[]):
        """set characteristics dictionary based on a list of integers
            rolls - list of integers corresponding to characteristics
                  - will default to all 0's if argument not provided """
        
        # if no rolls are provided, set all of them to 0
        # if wrong length of rolls print error and return
        if len(rolls) == 0:
            rolls = [0] * DChar.NUM_QUALITIES
        elif len(rolls) != DChar.NUM_QUALITIES:
            print(f'Attempt to set player characteristics with wrong length array')
            print(f'You provided {len(rolls)} rolls and you should have provided {DChar.NUM_QUALITIES}')
            return

        # map the rolls array to the characteristic dictionary
        for i in range(0, DChar.NUM_QUALITIES):
            self.characteristics[DChar.QUALITIES[i]]=rolls[i]

    def display_character(self):
        print_header(f"Player named '{self.player_name}' has the following Characteristics:")
        for key, value in self.characteristics.items():
            print(f'{key.title()} = {value}')
        print()
        
    def roll_character(self):
        """roll a character with all values >= than MIN_ROLL""" 
        attempts = 0
        # temp_roll is an array to store all rolls for a single character
        temp_roll = [0] * DChar.NUM_QUALITIES
        min_roll = 0 # value of smallest characteristics in last roll

        print_header(f'Rolling for characteristics of player named {self.player_name}', '-')

        # Roll all qualities and then check if all are greater than minimum
        while min_roll < DChar.MIN_ROLL:
            attempts += 1
            char_roll = [self.roll3() for x in temp_roll]  #roll all charateristics
            min_roll = min(char_roll)  # find min roll in charateristics
            if (attempts % 10_000 == 0):
                print(f'Still looking after {attempts} attempts ...')
            if (attempts % 10_000_000 == 0):
                print(f'I quit looking after {attempts} attempts!')
                min_roll = DChar.MIN_ROLL

        print(f'{attempts} attempts were made to roll a character '
              f'with all characteristics >= {DChar.MIN_ROLL}\n')

        self.set_characteristics(char_roll)

    def roll3(self):
        """Return the sum of 3 6-sided dice thrown simultaneously"""
        # randint is incredibly slow which is the bottleneck for the whole program
        return randint(1,6) + randint(1,6) + randint(1,6)

flach = DChar('Flach the Fearless')
seguso = DChar('Seguso the Strong')
print(f'Broken by The Nibbler\n')