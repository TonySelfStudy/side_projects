"""
Purpose: Simple project to utilize argparse, generator functions, and command line input.

Created by: Tony Held
Created on: 2021-03-06

References & Acknowledgements:
1) Inspired by `Impractical Python Projects` chapter 1 challenge
2) argument parser: https://docs.python.org/3/howto/argparse.html
3) Generator overview: https://realpython.com/introduction-to-python-generators/
"""

import sys
from random import choice
import argparse

# First and last silly name options for
first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
         "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
         'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
         'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
         'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
         'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
         'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
         'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
         '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
         'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
         'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
         "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
         'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
         'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
         "Winston 'Jazz Hands'", 'Worms')

middle = ('Logan', 'Lucas', 'Harry', 'Theo',  'Thomas',  'Brodie',  'Archie',  'Jacob',
          'Finlay',  'Finn',  'Daniel',  'Joshua',  'Oscar',  'Arthur',  'Hunter', 'Ethan',
          'Mason',  'Harrison',  'Freddie',  'Ollie',  'Adam',  'William',  'Jaxon',  'Aaron',
          'Cameron',  'Liam',  'George',  'Jamie',  'Callum',  'Matthew',  'Muhammad',  'Caleb',
          'Nathan',  'Tommy',  'Carter',  'Blake',  'Andrew',  'Luke',  'Jude',  'Angus')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')

class TooPicky(Exception):
    """Exception if the user does not select a name combo in a reasonable amount of tries."""
    pass

def name_combo(max_tries):
    """Return next choice via a generator function"""

    for i in range(max_tries):
        yield f"Try # {i}: {choice(first)} {choice(last)}"
    raise TooPicky("What's wrong with you! :)")


def main(max_tries=10):
    """Main function to drive silly name creator."""

    print("Welcome to the silly name generator.")
    print(f"You get a maximum of {max_tries} tries.")
    print("Press q<enter> to quit or <enter> to select again", flush=True)
    full_name = None

    try:
        for full_name in name_combo(max_tries):
            print(full_name, file=sys.stderr, end="")
            my_input = input()
            if my_input.lower() == "q":
                break
        print(f"Excellent choice!")
    except TooPicky as tp:
        print(tp)
        print("You are way too picky and can't select any more.")
        print(f"You are stuck with your last choice.")
    print(f"Your name is = {full_name}")


if __name__ == "__main__":
    """
    Silly name generator using command line arguments to decide number of
    naming attempts.
    
    Example usage:  
        python silly_names.py -max_tries 7
        python silly_names.py -m 3
    """
    parser = argparse.ArgumentParser(description='Silly name generator.')
    parser.add_argument('-m', '--max_tries', type=int)
    args = parser.parse_args()

    if args.max_tries is None:
        main()
    else:
        main(args.max_tries)
