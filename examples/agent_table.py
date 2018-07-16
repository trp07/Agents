"""
Example of a table-driven agent, see CH2 of AIMA.
"""

import time

from agentpy import agents

loc_A, loc_B = (0, 0), (0, 1)   # locations in a 2-D, two-room world


def TableVacuumProgram():
    """table defines the percept sequence to action mapping."""
    table = {
        ((loc_A, 'Clean'),): 'Right',
        ((loc_A, 'Dirty'),): 'Suck',
        ((loc_B, 'Clean'),): 'Left',
        ((loc_B, 'Dirty'),): 'Suck',
        ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
        ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
        ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
        ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
        ((loc_A, 'Dirty'), (loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
        ((loc_B, 'Dirty'), (loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
    }
    return agents.TableDrivenAgentProgram(table)


if __name__ == '__main__':

    program = TableVacuumProgram()
    a = agents.trace_agent(agents.Agent(program))

    percepts = [(loc_A, 'Clean'), (loc_A, 'Dirty'),
                (loc_B, 'Clean'), (loc_B, 'Dirty')]

    a.program((loc_A, 'Dirty'))
    time.sleep(1)
    a.program((loc_A, 'Clean'))
    time.sleep(1)
    a.program((loc_B, 'Dirty'))
    time.sleep(1)
    a.program( (loc_B, 'Clean'))
