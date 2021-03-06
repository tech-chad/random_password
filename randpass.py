import argparse
from random import choice
from random import shuffle

from typing import List
from typing import Optional
from typing import Sequence

UPPER_LETTERS = (x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER_LETTERS = (x for x in "abcdefghijklmnopqrstuvwxyz")
DIGITS = (x for x in "0123456789")
SPECIAL = [x for x in ".,*&^%$#@!-+=/_:;"]


def generate_password(possible: List[str], length: int, special: int) -> str:
    """ Generate one random password. """
    password = []
    if special:
        length -= special
        for x in range(special):
            password.append(choice(SPECIAL))
    while True:
        num = lower = upper = False  # making sure one of each
        characters = []
        for x in range(length):
            rand_char = choice(possible)
            if rand_char.isdigit():
                num = True
            elif rand_char.isupper():
                upper = True
            elif rand_char.islower():
                lower = True
            characters.append(rand_char)
        if num and lower and upper:
            break
    password.extend(characters)
    shuffle(password)
    return "".join(password)


def make_possible() -> List[str]:
    possible = []
    possible.extend(UPPER_LETTERS)
    possible.extend(LOWER_LETTERS)
    possible.extend(DIGITS)
    return possible


def save_to_file(filename: str, passwords: List[str]) -> None:
    with open(filename, "w") as f:
        for password in passwords:
            f.write(f"{password}\n")


def argument_parsing(args: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=10,
                        help="Length of the password (default 10)")
    parser.add_argument("-s", "--special", type=int, default=0,
                        help="Number of special char to use.")
    parser.add_argument("-n", "--number", type=int, default=1,
                        help="Number of passwords to generate")
    parser.add_argument("-o", "--output", type=str, default="", metavar="filename",
                        help="Save generated passwords to filename entered")
    return parser.parse_args(args)


def main(args: Optional[Sequence[str]] = None) -> int:
    password_list = []
    argv = argument_parsing(args)
    possible = make_possible()
    for x in range(argv.number):
        password = generate_password(possible, argv.length, argv.special)
        password_list.append(password)
        print(password)
    if argv.output:
        save_to_file(argv.output, password_list)
    return 0


if __name__ == "__main__":
    exit(main())
