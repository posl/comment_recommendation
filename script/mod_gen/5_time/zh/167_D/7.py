def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [0] * N
    visited[0] = 1
    i = 0
    while K > 0:
        i = A[i] - 1
        K -= 1
        if visited[i] == 1:
            break
        visited[i] = 1
    if K == 0:
        print(i + 1)
    else:
        K %= sum(visited)
        while K > 0:
            i = A[i] - 1
            K -= 1
        print(i + 1)
solve()
