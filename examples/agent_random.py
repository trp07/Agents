"""
Example of a random agent program.
"""
import time
from agentpy import agents


def randomPilotProgram() -> 'program':
    actions = ['Descend', 'Climb', 'Turn_Left', 'Turn_Right']
    return agents.RandomAgentProgram(actions)



if __name__ == '__main__':

    program = randomPilotProgram()
    a = agents.trace_agent(agents.Agent(program))

    for i in range(3):
        a.program(i)
        time.sleep(1)
