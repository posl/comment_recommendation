def solve():
    # N = int(input())
    # P = list(map(int, input().split()))
    N = 5
    P = [5, 3, 2, 4, 1]
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i + 1
    print(Q)
solve()
