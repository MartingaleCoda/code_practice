from dependency_injection import actions, factories


class TestActionFactory:
    def test_instantiates_phrases_action_if_num1_lt_0(self):
        random_number1 = -1
        random_number2 = 2
        action = factories.action_factory(
            random_number1=random_number1, random_number2=random_number2
        )
        assert action.__class__ is actions.PhrasesActor

    def test_instantiates_math_action_if_num1_eq_0(self):
        random_number1 = 0
        random_number2 = 2
        action = factories.action_factory(
            random_number1=random_number1, random_number2=random_number2
        )
        assert action.__class__ is actions.MathActor

    def test_instantiates_math_action_if_num1_gt_0(self):
        random_number1 = 1
        random_number2 = 2
        action = factories.action_factory(
            random_number1=random_number1, random_number2=random_number2
        )
        assert action.__class__ is actions.MathActor
