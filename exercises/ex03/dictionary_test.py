"""Tests the functions defined in dictionary.py"""

__author__: str = "730471166"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_use_1() -> None:
    """Use case test 1 for invert"""
    assert invert({"a": "1", "b": "2", "c": "3"}) == {"1": "a", "2": "b", "3": "c"}


def test_invert_use_2() -> None:
    """Use case test 2 for invert"""
    assert invert({"Lebron": "James", "Drake": "Maye", "Goat": "Status"}) == {
        "James": "Lebron",
        "Maye": "Drake",
        "Status": "Goat",
    }


def test_invert_edge_1() -> None:
    assert invert({}) == {}


def test_count_use_1() -> None:
    assert count(["apple", "pear", "apple"]) == {"apple": 2, "pear": 1}


def test_count_use_2() -> None:
    assert count(["y", "y", "y", "b", "b", "a"]) == {"y": 3, "b": 2, "a": 1}


def test_count_edge_1() -> None:
    assert count([]) == {}


def test_favorite_color_use_1() -> None:
    assert favorite_color({"Dean": "blue", "Roy": "green", "Hubert": "blue"}) == "blue"


def test_favorite_color_use_2() -> None:
    assert (
        favorite_color(
            {"Tyler": "red", "Cole": "green", "Lucas": "blue", "Jaden": "red"}
        )
        == "red"
    )


def test_favorite_color_edge_1() -> None:
    assert (
        favorite_color(
            {"Dean": "blue", "Roy": "green", "Hubert": "blue", "Mondo": "green"}
        )
        == "blue"
    )


def test_bin_len_use_1() -> None:
    assert bin_len(["cat", "dog", "bat"]) == {3: {"cat", "dog", "bat"}}


def test_bin_len_use_2() -> None:
    assert bin_len(["apple", "fig", "pear"]) == {5: {"apple"}, 3: {"fig"}, 4: {"pear"}}


def test_bin_len_edge_1() -> None:
    assert bin_len([]) == {}
