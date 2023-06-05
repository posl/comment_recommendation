def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    visited = [False] * n
    visited[0] = True
    current = 0
    for i in range(k):
        current = a[current] - 1
        if visited[current]:
            break
        visited[current] = True
    if i == k - 1:
        print(current + 1)
    else:
        print(a[current])
