def solve():
    from collections import deque
    from itertools import permutations
    from copy import deepcopy
    
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    
    def bfs(p):
        q = deque([p])
        visited = set()
        while q:
            p = q.popleft()
            if p in visited:
                continue
            visited.add(p)
            for i in range(8):
                if p[i] == i + 1:
                    continue
                for j in range(i + 1, 8):
                    if p[j] == j + 1:
                        continue
                    if p[i] == j + 1:
                        p[i], p[j] = p[j], p[i]
                        q.append(deepcopy(p))
                        p[i], p[j] = p[j], p[i]
        return visited
    
    visited = bfs(p)
    if (1, 2, 3, 4, 5, 6, 7, 8) in visited:
        print(0)
        return
    
    for p in permutations(range(1, 9)):
        if p in visited:
            print(1)
            return
    
    for p in permutations(range(1, 9)):
        if p[:4] in visited and p[4:] in visited:
            print(2)
            return
    
    print(-1)
    return

if __name__ == '__main__':
    solve()