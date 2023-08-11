"""
TOPICS
- interfaces
- dependency injection
- factories

THEME
- I have no idea. Maybe just print some stuff.

GENERAL NOTES:
- exec(open(filename).read()) runs a python script from within a python shell
- running modules (pip, pytest, pytest-mock) requires `python -m <module>` on Windows in a git bash shell
"""
import random

from dependency_injection.actions import Action
from dependency_injection.factories import action_factory


def action_user(action: Action):
    action.use_actions()


def run() -> None:
    print("Start!")

    random_number1 = random.randint(-10, 10)
    random_number2 = random.randint(1, 10)
    print(f"numbers: {random_number1}, {random_number2}")

    action = action_factory(
        random_number1=random_number1, random_number2=random_number2
    )
    action_user(action=action)

    print("Done!")


if __name__ == "__main__":
    run()
