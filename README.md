# Week 10 Coding #8: Haunted Hotel Sweep

## Summary

This assignment uses graphs to represent areas inside a haunted hotel and the connections between them. The graph is stored using an adjacency list, where each area maps to a list of neighboring areas.

Breadth-first search (BFS) explores the hotel level by level using a queue. Depth-first search (DFS) explores deeply into one path before backtracking, using a stack. Both traversals help visit connected areas in different orders.

The visited set is important because it prevents revisiting the same areas repeatedly. This avoids infinite loops in graphs with cycles and ensures each area is processed only once.

---

## Approach

- I used a dictionary as an adjacency list to represent the graph.
- In get_neighbors, I safely checked whether the area exists before returning neighbors.
- In has_path, I used BFS with a queue to search for the target area.
- I used a visited set in every traversal/search function to prevent repeated visits.
- In bfs_order, I used collections.deque to process areas in FIFO order.
- In dfs_order, I used a stack to process areas in LIFO order.
- I used reversed(graph[current]) in DFS so the final traversal follows the original neighbor order.
- In count_reachable_areas, I counted how many unique areas were visited from the starting area.

---

## Complexity

### get_neighbors

- *Time:* O(1)
- *Space:* O(1)
- *Why:* Dictionary lookup takes constant time and no extra large structures are created.

### has_path

- *Time:* O(V + E)
- *Space:* O(V)
- *Why:* In the worst case, every vertex and edge may be visited once. The queue and visited set can store up to all vertices.

### bfs_order

- *Time:* O(V + E)
- *Space:* O(V)
- *Why:* BFS visits every area and connection once while storing visited nodes and queue data.

### dfs_order

- *Time:* O(V + E)
- *Space:* O(V)
- *Why:* DFS may visit every node and edge once, while the stack and visited set store visited areas.

### Stretch: count_reachable_areas

- *Time:* O(V + E)
- *Space:* O(V)
- *Why:* The function performs a traversal through all reachable nodes and stores visited areas.

---

## Edge-Case Checklist

- [x] empty graph
- [x] missing start area
- [x] missing target area
- [x] start == target
- [x] graph with a cycle
- [x] disconnected graph
- [x] area with no neighbors

### Notes

- The visited set was especially important for handling cycles safely.
- Returning empty lists or False for missing areas prevented runtime errors.
- DFS neighbor order required careful handling using reversed().

---

## Tests Added

- Added a test for an empty graph.
- Added a test where start == target.
- Added a test for graphs with cycles to confirm no infinite loops occur.

---

## Known Limitations

```text
No known limitations.