"""Actions."""
import random
from typing import Type, TypeVar

from dependency_injection.interfaces import FormalActionInterface

Action = TypeVar("Action", bound=FormalActionInterface)

EXTRA_PHRASE = "I'm extra"
RANDOM_RANGE = (1, 5)


class PhrasesActor(FormalActionInterface):
    """Can print a phrase with some extra text and a number."""

    def __init__(self, phrase: str, number: int):
        self.phrase = phrase
        self.number = number
        self.extra = EXTRA_PHRASE

    def use_actions(self) -> None:
        self.print_extra()
        self.action1()
        self.action2()

    def print_extra(self) -> None:
        print(f"extra: {self.extra}")

    def action1(self) -> None:
        """Print phrase."""
        print(f"phrase: {self.phrase}")

    def action2(self) -> None:
        """Print number."""
        print(f"number: {self.number}")


class MathActor(FormalActionInterface):
    """Can print a sum or a product with some interference."""

    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2
        self.interference = random.randint(*RANDOM_RANGE)

    def use_actions(self) -> None:
        self.print_interference()
        self.action1()
        self.action2()

    def print_interference(self) -> None:
        print(f"interference: {self.interference}")

    def action1(self) -> None:
        """Print sum."""
        print(f"sum: {self.num1 + self.num2 + self.interference}")

    def action2(self) -> None:
        """Print product."""
        print(f"product: {self.num1 * self.num2 * self.interference}")
