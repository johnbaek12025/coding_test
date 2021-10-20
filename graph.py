from typing import List, Dict
from collections import defaultdict

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
def recursive_dfs(v: int, discovered: List[int] = []) -> List[int]:
    # dictionary 순
    discovered.append(v)

    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


def iterative_dfs(v: int) -> List[int]:
    # stack 역순 순
    discovered = []
    stack = [v]

    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v) 
            for w in graph[v]:
                stack.append(w)
    return discovered


def bfs(v: int) -> List[int]:
    discovered = [v]
    queue = [v]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered



print(recursive_dfs(1))
print(iterative_dfs(1))
print(bfs(1))