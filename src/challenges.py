from collections import deque

Graph = dict[str, list[str]]


def get_neighbors(graph: Graph, area: str) -> list[str]:
    """Return neighboring areas, or [] if the area is missing."""
    return graph.get(area, [])


def has_path(graph: Graph, start: str, target: str) -> bool:
    """Return True if target is reachable from start."""
    if start not in graph or target not in graph:
        return False
    if start == target:
        return True
    
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current = queue.popleft()
        for neighbor in get_neighbors(graph, current):
            if neighbor == target:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False


def bfs_order(graph: Graph, start: str) -> list[str]:
    """Return areas in breadth-first sweep order."""
    if start not in graph:
        return []
    
    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in get_neighbors(graph, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return order


def dfs_order(graph: Graph, start: str) -> list[str]:
    """Return areas in depth-first sweep order."""
    if start not in graph:
        return []
    
    visited = set()
    order = []
    stack = [start]
    
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            order.append(current)
            for neighbor in reversed(get_neighbors(graph, current)):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return order


def count_reachable_areas(graph: Graph, start: str) -> int:
    """Return how many unique areas are reachable from start."""
    if start not in graph:
        return 0
    
    return len(bfs_order(graph, start))