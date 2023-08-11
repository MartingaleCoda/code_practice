import random

from dependency_injection import actors


class TestPhrasesActor:
    test_data = {
        "phrase": "some_phrase",
        "number": 1,
        "extra": actors.EXTRA_PHRASE,
    }
    phrases_actor = actors.PhrasesActor(
        phrase=test_data["phrase"], number=test_data["number"]
    )

    def test_initializes_with_expected_data(self):
        for key, value in self.test_data.items():
            assert getattr(self.phrases_actor, key)

    def test_use_actions_calls_all_functions(self, mocker):
        expected_calls = (
            mocker.patch("dependency_injection.actors.PhrasesActor.print_extra"),
            mocker.patch("dependency_injection.actors.PhrasesActor.action1"),
            mocker.patch("dependency_injection.actors.PhrasesActor.action2"),
        )

        self.phrases_actor.use_actions()

        for mocked_function in expected_calls:
            assert mocked_function.called

    def test_print_extra_prints_extra_phrase(self, capfd):
        self.phrases_actor.print_extra()
        output, error = capfd.readouterr()
        assert output == f"extra: {actors.EXTRA_PHRASE}\n"

    def test_action1_prints_phrase(self, capfd):
        self.phrases_actor.action1()
        output, error = capfd.readouterr()
        assert output == f"phrase: {self.phrases_actor.phrase}\n"

    def test_action2_prints_number(self, capfd):
        self.phrases_actor.action2()
        output, error = capfd.readouterr()
        assert output == f"number: {self.phrases_actor.number}\n"


class TestPhrasesActor:
    seed = random.seed(1)
    test_data = {
        "num1": 2,
        "num2": 3,
        "interference": random.randint(*actors.RANDOM_RANGE),
    }
    math_actor = actors.MathActor(num1=test_data["num1"], num2=test_data["num2"])

    def test_initializes_with_expected_data(self):
        for key, value in self.test_data.items():
            assert getattr(self.math_actor, key)

    def test_use_actions_calls_all_functions(self, mocker):
        mocked = [
            mocker.patch("dependency_injection.actors.MathActor.print_interference"),
            mocker.patch("dependency_injection.actors.MathActor.action1"),
            mocker.patch("dependency_injection.actors.MathActor.action2"),
        ]

        self.math_actor.use_actions()

        for mocked_function in mocked:
            assert mocked_function.called

    def test_print_interference_prints_interference(self, capfd):
        self.math_actor.print_interference()
        output, error = capfd.readouterr()
        assert output == f"interference: {self.math_actor.interference}\n"

    def test_action1_prints_sum(self, capfd):
        self.math_actor.action1()
        output, error = capfd.readouterr()
        assert (
            output
            == f"sum: {self.math_actor.num1 + self.math_actor.num2 + self.math_actor.interference}\n"
        )

    def test_action2_prints_product(self, capfd):
        self.math_actor.action2()
        output, error = capfd.readouterr()
        assert (
            output
            == f"product: {self.math_actor.num1 * self.math_actor.num2 * self.math_actor.interference}\n"
        )
