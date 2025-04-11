"""Creates the playable game Worlde"""

__author__ = "730471166"


def contains_char(secret: str, letter: str) -> bool:
    """Determines if string input has matching characters"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    if secret[0] == letter:
        return True
    elif secret[1] == letter:
        return True
    elif secret[2] == letter:
        return True
    elif secret[3] == letter:
        return True
    elif secret[4] == letter:
        return True
    else:
        return False


def emojified(guess: str, correct: str) -> str:
    """Returns color coded boxes based on guess"""
    assert len(guess) == len(correct), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    x: int = 0
    final = ""
    while x < len(correct):
        if guess[x] == correct[x]:
            final += GREEN_BOX
        elif contains_char(correct, guess[x]):
            final += YELLOW_BOX
        else:
            final += WHITE_BOX
        x += 1
    return final


def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word: ")
    if len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    n: int = 1
    while n <= 6:
        print(f"=== Turn {n}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {n}/6 turns!")
            return
        n += 1
    if n >= 6:
        print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main(secret="codes")
