"""
Example of a reflex agent program.  see CH2 of AIMA.
"""
import time
import random
from agentpy import agents

loc_A, loc_B = (0, 0), (0, 1)   # locations in a 2-D, two-room world

RULES = [
    agents.RULE((loc_A, 'Clean'), 'Right'),
    agents.RULE((loc_A, 'Dirty'), 'Suck'),
    agents.RULE((loc_B, 'Clean'), 'Left'),
    agents.RULE((loc_B, 'Dirty'), 'Suck'),
]


def interpret_input(percept:str) -> 'percept':
    """No interpretation needed.  Just return the percept."""
    return percept


def reflexVaccumProgram() -> 'program':
    return agents.SimpleReflexAgentProgram(RULES, interpret_input)


if __name__ == '__main__':

    program = reflexVaccumProgram()
    a = agents.trace_agent(agents.Agent(program))

    percepts = [(loc_A, 'Clean'), (loc_A, 'Dirty'),
                (loc_B, 'Clean'), (loc_B, 'Dirty')]

    for i in range(5):
        a.program(random.choice(percepts))
        time.sleep(.5)
