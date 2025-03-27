# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.


import inspect
import sys
import random
from collections import deque
from heapq import heappush, heappop
sys.setrecursionlimit(10**9)

def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Method not implemented: %s at line %s of %s" % (method, line, fileName))
    sys.exit(1)


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        pass

    def isGoalState(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        pass

    def getSuccessors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        pass

    def getCostOfActions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        pass


def random_search(problem):
    """
    Search the nodes in the search tree randomly.

    Your search algorithm needs to return a list of actions that reaches the goal.
    Make sure to implement a graph search algorithm.

    This random_search function is just example not a solution.
    You can write your code by examining this function
    """
    start = problem.getStartState()
    node = [(start, "", 0)]   # class is better
    frontier = [node]

    explored = set()
    while frontier:
        node = random.choice(frontier)
        state = node[-1][0]
        if problem.isGoalState(state):
            return [x[1] for x in node][1:]

        if state not in explored:
            explored.add(state)

            for successor in problem.getSuccessors(state):
                if successor[0] not in explored:
                    parent = node[:]
                    parent.append(successor)
                    frontier.append(parent)

    return []


def depth_first_search(problem):
    """
    DFS로 최소 비용 경로를 보장하기 위한 최적화된 알고리즘.
    """
    def dfs(state, path, cost, visited, min_cost):
        # 목표 상태에 도달하면 최소 비용 갱신
        if problem.isGoalState(state):
            if cost < min_cost[0]:
                min_cost[0] = cost
                return path
            return None

        # 현재 상태를 방문 처리
        visited.add(state)

        best_path = None

        for successor, action, step_cost in problem.getSuccessors(state):
            # 다음 상태를 방문하지 않았거나 더 적은 비용으로 방문할 경우에만 탐색
            if successor not in visited or cost + step_cost < min_cost[0]:
                result = dfs(successor, path + [action], cost + step_cost, visited, min_cost)
                if result is not None:
                    best_path = result
                    print(result)

        # 상태를 백트래킹하여 방문 목록에서 제거
        visited.remove(state)

        return best_path

    # 초기화
    start_state = problem.getStartState()
    min_cost = [float('inf')]  # 최소 비용 저장
    visited = set()  # 방문한 상태 저장

    # DFS 호출
    return dfs(start_state, [], 0, visited, min_cost)



    


def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    start = problem.getStartState() # 처음 상태
    explored = set() # 방문 확인
    node = [(start, "", 0)] # 처음 노드 
    q = deque([node]) # 처음 노드 큐에 삽입

    while q:    #  q가 빌 때까지 반복
        node = q.pop() # q에서 요소 꺼내기
        state = node[-1][0] # 요소에서 state 저장
        if problem.isGoalState(state): # 정답인지 확인
            return [x[1] for x in node][1:] # 정답 일 시 정답 반환 
             
        if state not in explored: #
            explored.add(state) 
            for successor in problem.getSuccessors(state):
                if successor[0] not in explored:
                    parent = node[:]
                    parent.append(successor)
                    q.appendleft(parent)
        
                   
        




def uniform_cost_search(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    explored = set()
    pq = []  # 우선순위 큐
    heappush(pq, (0, [(start, "", 0)]))  # (총 비용, 노드 경로) 저장

    while pq:
        cost, node = heappop(pq)  # 최소 비용 노드 꺼냄
        state = node[-1][0]  # 현재 상태
        
        # 목표 상태 검사
        if problem.isGoalState(state):
            return [x[1] for x in node][1:]  # 경로 반환
        
        # 상태가 방문되지 않았으면 탐색
        if state not in explored:
            explored.add(state)
            
            # 후속 상태 탐색
            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in explored:
                    new_cost = cost + step_cost
                    new_path = node[:]  # 현재 경로 복사
                    new_path.append((successor, action, step_cost))
                    heappush(pq, (new_cost, new_path))  # 우선순위 큐에 추가

    return []  # 목표 상태를 찾지 못하면 빈 리스트 반환


def heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. This heuristic is trivial.
    """
    "*** YOUR CODE HERE ***"
    return 0


def aStar_search(problem, heuristic=heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    raiseNotDefined()


# Abbreviations
rand = random_search
bfs = breadth_first_search
dfs = depth_first_search
astar = aStar_search
ucs = uniform_cost_search
