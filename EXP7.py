graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

visited = set()
queue = ['A']

while queue:
    node = queue.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        queue.extend(graph[node])
