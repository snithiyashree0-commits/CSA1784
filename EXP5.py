from collections import deque

def valid(m, c):
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def solve():
    queue = deque([((3,3,1), [])])
    visited = set()

    while queue:
        (m,c,b), path = queue.popleft()

        if (m,c,b) == (0,0,0):
            print(path + [(0,0,0)])
            return

        if (m,c,b) in visited:
            continue

        visited.add((m,c,b))

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for dm, dc in moves:
            if b:
                nm, nc = m-dm, c-dc
            else:
                nm, nc = m+dm, c+dc

            nb = 1-b

            if 0 <= nm <= 3 and 0 <= nc <= 3 and valid(nm,nc):
                queue.append(((nm,nc,nb), path+[(m,c,b)]))

solve()
