from dependency_injection import actors, factories


class TestActorFactory:
    def test_instantiates_phrases_action_if_num1_lt_0(self):
        random_number1 = -1
        random_number2 = 2
        actor = factories.actor_factory(
            random_number1=random_number1, random_number2=random_number2
        )
        assert actor.__class__ is actors.PhrasesActor

    def test_instantiates_math_action_if_num1_eq_0(self):
        random_number1 = 0
        random_number2 = 2
        actor = factories.actor_factory(
            random_number1=random_number1, random_number2=random_number2
        )
        assert actor.__class__ is actors.MathActor

    def test_instantiates_math_action_if_num1_gt_0(self):
        random_number1 = 1
        random_number2 = 2
        actor = factories.actor_factory(
            random_number1=random_number1, random_number2=random_number2
        )
        assert actor.__class__ is actors.MathActor
