# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self): #functia returneaza start state ul pt problema
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state): #functia returneaza true daca state ul este valid
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state): # returneaza l lista de actiuni
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    nodesToBeExplored = util.Stack() #stiva pentru nodurile pe care trebuie sa le exploram
    visited = [] #lista pentru a tine evidenta starilor vizitate
    initial_state = problem.getStartState() #starea initiala
    nodesToBeExplored.push((initial_state,[])) #punem pe stiva starea initiala si o lista goala de actiuni

    #exploram pana cand stiva este goala
    while (nodesToBeExplored.isEmpty() != True):

        current, actionsToDo = nodesToBeExplored.pop() #starea curenta si actiunile ei

        #verificare daca starea curenta este starea scop si daca da return la actiunile ei
        if(problem.isGoalState(current)):
            return actionsToDo
        
        #daca starea nu e scop si nu a fost vizitata
        if(current not in visited):

            visited.append(current) #o vizitam
            nodes = problem.expand(current) #expandam pentru a obtine starile urmatoare

            for next,action,_ in nodes:
                new_actionsToDo = actionsToDo + [action]
                nodesToBeExplored.push((next,new_actionsToDo))#introducem urmatoarea stare si noua lista de actiuni in stiva pentru a fi explorata
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    source = problem.getStartState() # accesam nodul sursa
    if problem.isGoalState(source): # verificam daca nodul sursa este si destinatie
        return []

    reached = []    # o lista pentru nodurile pe care le-am expandat pana in prezent

    frontier = util.PriorityQueue() # o lista de prioritate pentru nodurile pe care trebuie sa le procesam
    frontier.push((source, [], 0), 0) # initializam frontiera cu nodul sursa

    while not frontier.isEmpty(): # cat timp mai sunt noduri de procesat

        current_node, actions, current_cost = frontier.pop() # procesam nodul cu costul cel mai mic

        if current_node not in reached: # daca nodul nu a fost expandat pana acum il expandam
            reached.append(current_node) 

            if problem.isGoalState(current_node): #verificam daca reprezinta nodul destinatie
                return actions # returnam lista de actiuni pentru a ajunge din sursa in destinatie

            for child, action, cost in problem.expand(current_node): # pentru fiecare copil al nodului
                child_action = actions + [action] # actualizam actiunile
                child_cost = current_cost + cost    # actualizam costul pentru a ajunge din sursa in nodul copil
                total_cost = child_cost + heuristic(child,problem) # actualizam costul total cu tot cu functie heuristica
                frontier.push((child, child_action, child_cost),total_cost) # introducem nodul copil in frontiera pentru a fi expandat
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
