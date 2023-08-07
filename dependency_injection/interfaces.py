"""Interfaces."""
import abc


class FormalActionInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return all(
            (
                hasattr(subclass, "action1"),
                callable(subclass.action1),
                hasattr(subclass, "action2"),
                callable(subclass.action2),
            )
        )

    @abc.abstractmethod
    def action1(self, phrase: str):
        """Do action 1."""
        raise NotImplementedError

    @abc.abstractmethod
    def action2(self, number: int):
        """Do action 2."""
        raise NotImplementedError
