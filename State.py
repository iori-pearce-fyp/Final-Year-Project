class State:
    def __init__(self, state):
        if not isinstance(state, str):
            raise ValueError("State input not valid")
        self._state_name = state
    
    def get_state_name(self):
        return self._state_name