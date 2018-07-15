"""Agents, objects, and environments."""

import collections
from abc import ABCMeta


"""###########################################################################
Abstract Classes:
1. Thing: abstract class for other objects that can exist in the environment.
    You make "things" with Thing.
2. Agent: superclass for agents to inherit from.  Inherits from Thing.

Utility Functions:
1. trace_agent: replace the agent.program function with one that prints
    input/outputs to the screen, so you can see the agent in the environment.
"""

class Thing(metaclass=ABCMeta):
    """Abstract class for any object in the environment to inherit from.
    Make "things" out of the Thing class.
    """

    def __repr__(self):
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))


    def is_alive(self):
        """Things that are 'alive' should return True."""
        return hasattr(self, 'alive') and self.alive


    def show_state(self):
        """Display the agent's internal state. Subclasses should override."""
        print("I don't know how to show_state.")



class Agent(Thing):
    """Superclass for all agents. Inherits from Thing.

    Args:
        * program: (function/callable) Not to be defined as a method, but an
            attribute that is callable and accepts a percept as an argument.
            That way the program can only look at the percept and not have any
            knowledge about the agent.  When called, returns an action.

    Attributes:
        * alive: (bool)
        * bump: (bool)
        * holding: (list)
        * performance: (int) optional measure of performance in the agent's
            environment.
    """

    def __init__(self, program=None):
        self.alive = True
        self.bump = False
        self.holding = []
        self.performance = 0
        if program is None or not isinstance(program, collections.Callable):
            raise AttributeError('program must be a callable')
        self.program = program


    def can_grab(self, thing):
        """Override in subclasses if the agent can grab 'thing'."""
        return False



def trace_agent(agent:'agent') -> 'agent':
    """Wraps an agent's program function and prints the
    inputs/outputs, so you can watch it in its environment.
    """
    old_program = agent.program
    def new_program(percept):
        action = old_program(percept)
        print('{} perceives <{}> and does <{}>'.format(agent, percept, action))
        return action
    agent.program = new_program
    return agent



"""###########################################################################
Generic Agent Programs:
1. TableDrivenAgentProgram: percepts map to actions based on table values.
2. RandomAgentProgram: choose an action at random from a list of actions.
3. SimpleReflexAgentProgram: action based solely on the current percept.
4. ModelBasedReflexAgentProgram: action based on percept and state

Utility Functions:
1. rule_match: return a rule from a given state
2. RULE: defines a namedtuple for a 'rule'
"""

def TableDrivenAgentProgram(table:dict) -> 'program':
    """This agent selects an action based on the percept sequence.
    It is practical only for tiny domains.
    To customize it, provide as table a dictionary of all
    {percept_sequence:action} pairs."""
    percepts = []
    def program(percept):
        percepts.append(percept)
        action = table.get(tuple(percepts))
        return action
    return program


def RandomAgentProgram(actions:list) -> 'program':
    """An agent that chooses an action at random, ignoring all percepts."""
    return lambda percept: random.choice(actions)


def SimpleReflexAgentProgram(rules:list, interpret_input:'function') -> 'program':
    """This agent takes action based solely on the percept."""
    def program(percept):
        state = interpret_input(percept)
        rule = rule_match(state, rules)
        action = rule.action
        return action
    return program


def ModelBasedReflexAgentProgram(rules:list, update_state:'function',
    model:dict) -> 'program':
    """This agent takes action based on the percept and state."""
    def program(percept):
        program.state = update_state(program.state, program.action, percept, model)
        rule = rule_match(program.state, rules)
        action = rule.action
        return action
    program.state = program.action = None
    return program


def rule_match(state:str, rules:list) -> 'rule':
    """Find the first RULE that matches state.
    'rules' should be a list of namedtuples with an 'action' attribute.
    Returns a NoOp RULE if no rule found.
    """
    for rule in rules:
        if rule.name == state:
            return rule
    return RULE('default', 'NoOp')


RULE = collections.namedtuple('rule', 'name action')
