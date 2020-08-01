import argparse
from random import choice

from typing import List
from typing import Optional
from typing import Sequence

UPPER_LETTERS = (x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER_LETTERS = (x for x in "abcdefghijklmnopqrstuvwxyz")
DIGITS = (x for x in "0123456789")
SPECIAL = (x for x in ".,*&^%$#@!-+=/_:;")


def generate_password(possible: List[str], length: int) -> str:
    """ Generate one random password. """
    num = lower = upper = False
    while True:
        password = ""
        for _ in range(length):
            rand_char = choice(possible)
            # Make sure that at least one of each is used.
            if rand_char.isdigit():
                num = True
            elif rand_char.islower():
                lower = True
            elif rand_char.isupper():
                upper = True
            password += rand_char
        if num is True and lower is True and upper is True:
            break
    return password


def make_possible() -> List[str]:
    possible = []
    possible.extend(UPPER_LETTERS)
    possible.extend(LOWER_LETTERS)
    possible.extend(DIGITS)
    return possible


def argument_parsing(args: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=10,
                        help="Length of the password (default 10)")

    return parser.parse_args(args)


def main(args: Optional[Sequence[str]] = None) -> int:
    argv = argument_parsing(args)
    possible = make_possible()
    password = generate_password(possible, argv.length)
    print(password)
    return 0


if __name__ == "__main__":
    exit(main())
