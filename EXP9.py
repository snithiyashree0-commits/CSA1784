from itertools import permutations

graph = {
    0:{1:10,2:15,3:20},
    1:{0:10,2:35,3:25},
    2:{0:15,1:35,3:30},
    3:{0:20,1:25,2:30}
}

cities = [1,2,3]
min_path = float('inf')

for perm in permutations(cities):
    cost = 0
    k = 0

    for j in perm:
        cost += graph[k][j]
        k = j

    cost += graph[k][0]
    min_path = min(min_path, cost)

print("Minimum Cost:", min_path)
