class Environment():
    myGraph = {'s': set(['1','3']),
               '1': set(['g']),
               '2': set(['1']),
               '3': set(['1','g','4']),
               '4': set(['2', '5']),
               '5': set(['g', '2']),
               'g': set(['4'])}

    cost = {str(['s','1']): '2', str(['s','3']): '5',
            str(['3','1']): '5', str(['3','4']): '2', str(['3','g']): '6',
            str(['1','g']): '1',
            str(['g','4']): '7',
            str(['4','5']): '3', str(['4','2']): '4',
            str(['5','2']): '6', str(['5','g']): '3',
            str(['2','1']): '4',}

    start = 's'
    goal = 'g'

class Agent(Environment):
    # depth first search
    def DFS(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack: # if there are things in the stack...
            (vertex, path) = stack.pop() # remove things from the stack
            for next in graph[vertex] - set(path): # go to places not been in before
                if next == goal:
                    p.append(path + [next]) # keep a record of where been
                else:
                    stack.append((next, path + [next]))
        return p

    # breadth first search
    def BFS(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack: # if there are things in the stack...
            (vertex, path) = stack.pop(0) # remove things from the stack
            for next in graph[vertex] - set(path): # go to places not been in before
                if next == goal:# if reached where you are going
                    p.append(path + [next]) # keep a record of where been
                    return p
                else:
                    stack.append((next, path + [next]))
        return p

    def get_cost(path_to_cost):
        path_cost = 0
        i = 0 # counter to manipulate a loop
        while i < len(path_to_cost) - 1: # -1 so it doesnt go out of bounds, while is to add up all the costs
            l = []
            l.append(path_to_cost[i]) # first node
            l.append(path_to_cost[i + 1]) # second node
            path_cost = path_cost + int(Environment.cost[str(l)]) # read cost between the nodes (1 and 2)
            i += 1
        return path_cost

    # uniform cost search
    def UCS(graph, start, goal):
        stack = [(start, [start])]
        p = []
        least_cost = 1000 # goot to start high so you cut it down
        while stack: # if there are things in the stack...
            (vertex, path) = stack.pop() # remove things from the stack
            for next in graph[vertex] - set(path): # go to places not been in before
                if next == goal: # if reached where you are going, calculate cost
                    path_cost = Agent.get_cost(path + [next]) # to describe the journey covered
                    print('UCS path:', path + [next], 'Path cost:', path_cost)
                    print()
                    # out of all journeys cost, which is the best/ cheapest?
                    if path_cost < least_cost:
                        least_cost = path_cost
                        p = path + [next] # overides whatever was there
                   # p.append(path + [next]) # keep a record of where been
                else:
                    stack.append((next, path + [next]))
        return p

    def __init__(self, Environment):
        print('DFS Longest path', Agent.DFS(Environment.myGraph, Environment.start, Environment.goal)) # calling the function
        print('BFS Shortest path', Agent.BFS(Environment.myGraph, Environment.start, Environment.goal))
        print('UCS Cheapest Path', Agent.UCS(Environment.myGraph, Environment.start, Environment.goal))

theEnvironment = Environment()
theAgent = Agent(theEnvironment)
