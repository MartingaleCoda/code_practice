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
                hasattr(subclass, "use_actions"),
                callable(subclass.use_actions),
            )
        )

    @abc.abstractmethod
    def use_actions(self):
        """Use all actions and anything else needed as part of using actions."""
        raise NotImplementedError

    @abc.abstractmethod
    def action1(self):
        """Do action 1."""
        raise NotImplementedError

    @abc.abstractmethod
    def action2(self):
        """Do action 2."""
        raise NotImplementedError
