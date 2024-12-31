class State:
    def __init__(self, state):
        if not isinstance(state, str):
            raise ValueError("State input not valid")
        self._state_name = state
    

    """
    Function that will see if a different State object has the same state name
    Returns True if they do and False otherwise
    """
    def __eq__(self, other):
        # Check if other is also a State and compare the symbol
        if isinstance(other, State):
            return self._state_name == other._state_name
        return False


    """
    Function that will return the hashed value of the symbol
    """
    def __hash__(self):
        return hash(self._state_name)