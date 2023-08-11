from dependency_injection import interfaces, main


class TestRun:
    def test_run_calls_action_functions(self, mocker):
        expected_calls = (
            mocker.patch("dependency_injection.main.action_factory"),
            mocker.patch("dependency_injection.main.action_user"),
        )

        main.run()

        for mocked_function in expected_calls:
            assert mocked_function.called
