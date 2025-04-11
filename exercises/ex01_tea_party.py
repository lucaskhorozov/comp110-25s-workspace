"""A function to calculate cost for a teaparty"""

__author__: str = "730471166"


def main_planner(guests: int) -> None:
    """Entrypoint to tea party planner"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Number of teabags needed for x people"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed for x people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates cost for teabags and treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
