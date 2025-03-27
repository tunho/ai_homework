from eightpuzzle import createRandomEightPuzzle, EightPuzzleSearchProblem
from search import rand, bfs, dfs, astar, ucs
import time

if __name__ == '__main__':
  search_algorithms = [rand, bfs]
  random_search_running_time = []
  breadth_first_search_running_time = []
  for _ in range(100):
    puzzle = createRandomEightPuzzle(50)
    

    problem = EightPuzzleSearchProblem(puzzle)
    for alg in search_algorithms:
            start_time = time.time()
            alg(problem)
            end_time = time.time()
            execution_time = end_time - start_time
            if alg.__name__ == "random_search":
                random_search_running_time.append(execution_time)
            elif alg.__name__ == "breadth_first_search":
                breadth_first_search_running_time.append(execution_time)
  R_rounded_times = [round(num, 3) for num in random_search_running_time]
  B_rounded_times = [round(num, 3) for num in breadth_first_search_running_time]
  print(f"랜덤 서치 알고리즘: {R_rounded_times}")
  print(f"넓이 우선 서치치 알고리즘: {B_rounded_times}")
  print(f"랜덤 서치 평균시간: {round(sum(random_search_running_time)/100, 3)}입니다.")
  print(f"넓이 우선 평균시간: {round(sum(breadth_first_search_running_time)/100, 3)}입니다.")