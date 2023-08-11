from dependency_injection.actions import Action, MathActor, PhrasesActor


def action_factory(random_number1: int, random_number2: int) -> Action:
    """Decides which class to construct and returns an instance of that class with the parameters given."""
    if random_number1 < 0:
        phrase = f"ya, dyood. We got {random_number1}"
        return PhrasesActor(phrase=phrase, number=random_number2)
    return MathActor(num1=random_number1, num2=random_number2)
