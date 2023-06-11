from typing import Any


class State:
    """
    represents a state with all it's transitions
    """

    def __init__(self, value: Any) -> None:
        self.value = value
        self.transitions = {}

    def add_transition(self, value: Any, state: 'State') -> None:
        self.transitions[value] = state

    def next_state(self, value) -> 'State':
        """
        take action with some value in a state

        :param value: a value to validate
        :return: next state
        """

        return self.transitions.get(value, self)
