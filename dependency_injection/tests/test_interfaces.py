import pytest

from dependency_injection import interfaces

"""Child classes for testing implementation."""


class MissingUseActionsAction(interfaces.FormalActionInterface):
    def action1(self):
        pass

    def action2(self):
        pass


class MissingAction1Action(interfaces.FormalActionInterface):
    def use_actions(self):
        pass

    def action2(self):
        pass


class MissingAction2Action(interfaces.FormalActionInterface):
    def use_actions(self):
        pass

    def action1(self):
        pass


class AllActionsAction(interfaces.FormalActionInterface):
    def use_actions(self):
        pass

    def action1(self):
        pass

    def action2(self):
        pass


"""Tests."""


class TestFormalActionInterface:
    def test_subclasshook(self):
        assert issubclass(interfaces.FormalActionInterface, AllActionsAction)

    def test_missing_use_actions_raises_type_error(self):
        with pytest.raises(TypeError):
            MissingUseActionsAction()

    def test_missing_action1_raises_not_implemented_error(self):
        with pytest.raises(TypeError):
            MissingAction1Action()

    def test_missing_action2_raises_not_implemented_error(self):
        with pytest.raises(TypeError):
            MissingAction2Action()

    def test_child_class_instantiates_if_all_methods_are_implemented(self):
        assert AllActionsAction()
