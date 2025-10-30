import sys
from collections import deque
from typing import List, Tuple, Dict

Coord = Tuple[int, int]
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def read_maze(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    return [list(row) for row in lines]

def find_points(maze: List[List[str]])-> Tuple[Coord, Coord]:
    start = target = None
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == 'S': start = (r, c)
            if ch == 'T': target = (r, c)
    return start, target

def in_bounds(maze: List[List[str]], r: int, c: int) -> bool:
    return 0<=r<len(maze) and 0<=c<len(maze[0])

def neighbors(maze: List[List[str]], node: Coord) -> List[Coord]:
    r, c = node
    cand = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    res =[]
    for nr, nc in cand:
        if in_bounds(maze, nr, nc) and maze[nr][nc] != '#':
            res.append((nr, nc))

    return res

def reconstruct_path(parents: Dict[Coord, Coord] , start: Coord, target: Coord) -> List[Coord]:
    if target not in parents and target != start:
        return []

    path = [target]
    current = target
    while current != start:
        current = parents[current]
        path.append(current)

    path.reverse()
    return path

def bfs(maze: List[List[str]], start: Coord, target: Coord) -> List[Coord]:
    q = deque([start])
    visited = {start}
    parents: Dict[Coord, Coord] = {}
    while q:
        node = q.popleft()
        if node == target:
            return reconstruct_path(parents, start, target)
        for n in neighbors(maze, node):
            if n not in visited:
                visited.add(n)
                parents[n] = node
                q.append(n)

    return []

def dfs(maze: List[List[str]], start: Coord, target: Coord) -> List[Coord]:
    stack = [start]
    visited = {start}
    parents: Dict[Coord, Coord] = {}
    while stack:
        current = stack.pop()
        if current == target:
            return reconstruct_path(parents, start, target)
        for n in neighbors(maze, current):
            if n not in visited:
                visited.add(n)
                parents[n] = current
                stack.append(n)
    return []


def render_with_path(grid: List[List[str]], path: List[Coord], start: Coord, target: Coord) -> None:
    path_set = set(path)
    for r, row in enumerate(grid):
        out_line = []
        for c, ch in enumerate(row):
            pos = (r, c)
            if pos == start:
                out_line.append(f"{YELLOW}S{RESET}")
            elif pos == target:
                out_line.append(f"{GREEN}T{RESET}")
            elif pos in path_set and pos not in (start, target):
                out_line.append(f"{RED}*{RESET}")
            else:
                out_line.append(ch)
        print("".join(out_line))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python ex05.py <1-7>")
        sys.exit(1)

    nr = int(sys.argv[1])
    maze = read_maze(f"C:\\Users\\crist\\OneDrive\\Desktop\\utcn\\anIII_semI\\AI\\asg2\\lab02-cristinapop27\\maze{nr}.txt")
    start, target = find_points(maze)
    path= bfs(maze, start, target)
    render_with_path(maze, path, start, target)
