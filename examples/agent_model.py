"""
Example of a reflex agent program.  see CH2 of AIMA.
"""
import random
import time

from agentpy import agents

loc_A, loc_B = (0, 0), (0, 1)   # locations in a 2-D, two-room world


RULES = [
    agents.RULE((loc_A, 'Clean'), 'Right'),
    agents.RULE((loc_A, 'Dirty'), 'Suck'),
    agents.RULE((loc_B, 'Clean'), 'Left'),
    agents.RULE((loc_B, 'Dirty'), 'Suck'),
    agents.RULE(((loc_A, loc_B), 'Clean'), 'NoOp'),  # NoOp of both places clean
]


def update_state(state:str, action:str, percept:str, model:dict) -> 'state':
    """Update the model's current state.
    This simply just checks if each location is clean, and if so returns
    a RULE with a 'NoOP' action."""
    model[percept[0]] = percept[1]      # model[location] = state
    print('<Updated Model>...', model)
    if model[loc_A] == model[loc_B] == 'Clean':
        return ((loc_A, loc_B), 'Clean')
    else:
        return percept


def modelVacuumProgram():
    """An agent that keeps track of what locations are clean or dirty."""
    model = {loc_A: None, loc_B: None}
    return agents.ModelBasedReflexAgentProgram(RULES, update_state, model)



if __name__ == '__main__':

    program = modelVacuumProgram()
    a = agents.trace_agent(agents.Agent(program))

    percepts = [(loc_A, 'Clean'), (loc_A, 'Dirty'),
                (loc_B, 'Clean'), (loc_B, 'Dirty')]

    for i in range(5):
        a.program(random.choice(percepts))
        time.sleep(.5)
