"""
Purpose: Simple project to explore argparse (python's argument parser framework).

Created by: Tony Held
Created on: 2021-03-07

References & Acknowledgements:
1) argument parser: https://docs.python.org/3/howto/argparse.html
"""

import argparse

def settings_v01():
    """Argument handling configuration #1."""

    parser = argparse.ArgumentParser()
    parser.add_argument('echo', help="echo the string you use here")
    parser.add_argument("square", help="display a square of a given number", type=int)
    parser.add_argument("-v", "--verbosity", help="increase output verbosity")
    parser.add_argument("-d", "--debug_mode", help="flag to indicate using debug mode",
                        action="store_true")

    args = parser.parse_args()

    print(f"Echoing your first argument: {args.echo}")
    print(f'{args.square}^2 is {args.square**2} ')

    if args.verbosity:
        print(f'verbosity turned on.')
        print(f'\t{args.verbosity=}')

    if args.debug_mode:
        print(f'debug  mode turned on.')
        print(f'\t{args.debug_mode=}')
        print(f'\t{args=}')

def settings_v02():
    """Argument handling configuration #1."""
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="display a square of a given number", type=int)
    parser.add_argument('-v', '--verbose', action="store_true")
    args = parser.parse_args()

    value = args.number ** 2
    if args.verbose:
        print(f'Input value: {args.number}.  Its square is: {value}')
    else:
        print(f'{value}')

def settings_v03():
    """Argument handling configuration #1."""
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="display a square of a given number", type=int)
    parser.add_argument('-v', '--verbose', choices=[0, 1, 2], type=int)
    args = parser.parse_args()
    print(f'\t{args=}')

    value = args.number ** 2

    if (args.verbose is None) or (args.verbose == 0):
        print(f'{value}')
    elif args.verbose == 1:
        print(f'{args.number}^2 = {value}')
    else:
        print(f'Input value: {args.number}.  Its square is: {value}')

def settings_v04():
    """Argument handling configuration #1."""
    parser = argparse.ArgumentParser(description="Calculate X to the power of Y")
    parser.add_argument("base", help="display a square of a given number", type=int)
    parser.add_argument("exponent", help="display a square of a given number", type=int)
    parser.add_argument('-v', '--verbose', choices=[0, 1, 2], type=int)
    args = parser.parse_args()
    print(f'\t{args=}')

    value = args.base ** args.exponent

    if (args.verbose is None) or (args.verbose == 0):
        print(f'{value}')
    elif args.verbose == 1:
        print(f'{args.base}^{args.exponent} = {value}')
    else:
        print(f'Input value: {args.base}.  Raised to the {args.exponent} power it is: {value}')


if __name__ == "__main__":
    """Uncomment one setting below to have its function parse the command line arguments."""
    # settings_v01()
    # settings_v02()
    # settings_v03()
    settings_v04()
