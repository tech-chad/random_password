from random import choice

from typing import List

UPPER_LETTERS = (x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER_LETTERS = (x for x in "abcdefghijklmnopqrstuvwxyz")
DIGITS = (x for x in "0123456789")
SPECIAL = (x for x in ".,*&^%$#@!-+=/_:;")


def generate_password(possible: List[str]) -> str:
    """ Generate one random password. """
    num = lower = upper = False
    while True:
        password = ""
        for _ in range(10):
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


def main() -> int:
    possible = make_possible()
    password = generate_password(possible)
    print(password)
    return 0


if __name__ == "__main__":
    exit(main())
