"""Actions."""
from typing import Type, TypeVar

from interfaces import FormalActionInterface

Action = TypeVar("Action", bound="FormalActionInterface")


class PhrasesAction(FormalActionInterface):
    """Can print a phrase and a number."""

    def __init__(self, phrase: str, number: int):
        self.phrase = phrase
        self.number = number

    def action1(self) -> str:
        print(f"phrase: {self.phrase}")

    def action2(self) -> str:
        print(f"number: {self.number}")


class MathAction(FormalActionInterface):
    """Can print a sum and a product."""

    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def action1(self) -> str:
        print(f"sum: {self.num1 + self.num2}")

    def action2(self) -> str:
        print(f"product: {self.num1 * self.num2}")
