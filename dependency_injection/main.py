"""
TOPICS
- interfaces
- dependency injection
- factories

THEME
- I have no idea. Maybe just print some stuff.

GENERAL NOTES:
- exec(open(filename).read()) runs a python script from within a python shell
"""
import random

from actions import Action
from factories import action_factory


def main() -> None:
    random_number1 = random.randint(-10, 10)
    random_number2 = random.randint(1, 10)
    print(f"numbers: {random_number1}, {random_number2}")

    action = action_factory(
        random_number1=random_number1, random_number2=random_number2
    )
    action.use_actions()


if __name__ == "__main__":
    main()
