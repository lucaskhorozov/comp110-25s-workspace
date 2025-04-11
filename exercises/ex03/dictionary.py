"""Stores the functions for exercise three"""

__author__: str = "730471166"


def invert(og_dict: dict[str, str]) -> dict[str, str]:
    verted = {}
    for key in og_dict:
        value = og_dict[key]
        if value in verted:
            raise KeyError(f"This key already exists! : {value}")
        verted[value] = key
    return verted


def count(numbs: list[str]) -> dict[str, int]:
    final = {}
    x = 0
    while x < len(numbs):
        item = numbs[x]
        if item in final:
            final[item] = final[item] + 1
        else:
            final[item] = 1
        x += 1
    return final


def favorite_color(colors: dict[str, str]) -> str:
    final = []
    for name in colors:
        final.append(colors[name])
    counter = count(final)
    popular = ""
    highest = 0
    for color in counter:
        if counter[color] > highest:
            popular = color
            highest = counter[color]
    return popular


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    bin = {}
    for word in strings:
        length = len(word)
        if length not in bin:
            bin[length] = set()
        bin[length].add(word)
    return bin
