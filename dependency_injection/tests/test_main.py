from dependency_injection import interfaces, main


class AllActionsActor(interfaces.FormalActorInterface):
    def use_actions(self):
        pass

    def action1(self):
        pass

    def action2(self):
        pass


class TestActionUser:
    def test_action_user_calls_use_actions(self, mocker):
        actor = AllActionsActor()

        expected_calls = (mocker.patch("tests.test_main.AllActionsActor.use_actions"),)

        main.action_user(actor=actor)

        for mocked_function in expected_calls:
            assert mocked_function.called


class TestRun:
    def test_run_calls_action_functions(self, mocker):
        expected_calls = (
            mocker.patch("dependency_injection.main.actor_factory"),
            mocker.patch("dependency_injection.main.action_user"),
        )

        main.run()

        for mocked_function in expected_calls:
            assert mocked_function.called
