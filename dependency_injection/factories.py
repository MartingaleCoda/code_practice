from actions import Action, MathAction, PhrasesAction


def action_factory(random_number1: int, random_number2: int) -> Action:
    if random_number1 < 0:
        phrase = f"ya, dyood. We got {random_number1}"
        return PhrasesAction(phrase=phrase, number=random_number2)
    return MathAction(num1=random_number1, num2=random_number2)
