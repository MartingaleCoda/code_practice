import pytest

from dependency_injection import interfaces

"""Child classes for testing implementation."""


class MissingUseActionsActor(interfaces.FormalActorInterface):
    def action1(self):
        pass

    def action2(self):
        pass


class MissingAction1Actor(interfaces.FormalActorInterface):
    def use_actions(self):
        pass

    def action2(self):
        pass


class MissingAction2Actor(interfaces.FormalActorInterface):
    def use_actions(self):
        pass

    def action1(self):
        pass


class AllActionActor(interfaces.FormalActorInterface):
    def use_actions(self):
        pass

    def action1(self):
        pass

    def action2(self):
        pass


"""Tests."""


class TestFormalActorInterface:
    def test_subclasshook(self):
        assert issubclass(interfaces.FormalActorInterface, AllActionActor)

    def test_missing_use_actions_raises_type_error(self):
        with pytest.raises(TypeError):
            MissingUseActionsActor()

    def test_missing_action1_raises_not_implemented_error(self):
        with pytest.raises(TypeError):
            MissingAction1Actor()

    def test_missing_action2_raises_not_implemented_error(self):
        with pytest.raises(TypeError):
            MissingAction2Actor()

    def test_child_class_instantiates_if_all_methods_are_implemented(self):
        assert AllActionActor()
