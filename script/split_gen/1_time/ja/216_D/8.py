def solve():
    import sys
    readline = sys.stdin.readline
    N, M = map(int, readline().split())
    A = [0] * (N+1)
    for _ in range(M):
        K = int(readline())
        for a in map(int, readline().split()):
            A[a] += 1
    for a in A:
        if a % 2 != 0:
            print('No')
            return
    print('Yes')
    return
