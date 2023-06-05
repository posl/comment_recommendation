def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k -= 1
    visited = [False] * n
    visited[0] = True
    path = [0]
    while k:
        k -= 1
        path.append(a[path[-1]] - 1)
        if visited[path[-1]]:
            break
        visited[path[-1]] = True
    if k:
        print(path[k % len(path)] + 1)
    else:
        print(path[-1] + 1)
