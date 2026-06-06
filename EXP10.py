import heapq

graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',3),('E',6)],
    'C':[('F',5)],
    'D':[],
    'E':[('F',1)],
    'F':[]
}

heuristic = {
    'A':6,
    'B':4,
    'C':4,
    'D':2,
    'E':1,
    'F':0
}

def astar(start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Goal Reached:", node)
            return

        if node in visited:
            continue

        visited.add(node)

        for neigh, weight in graph[node]:
            heapq.heappush(
                pq,
                (cost + weight + heuristic[neigh], neigh)
            )

astar('A', 'F')
