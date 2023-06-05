def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    maxA = [0] * N
    minA = [0] * N
    maxA[0] = A[0]
    minA[0] = A[0]
    for i in range(1, N):
        maxA[i] = max(maxA[i - 1], A[i])
        minA[i] = min(minA[i - 1], A[i])
    res = 0
    for i in range(N):
        if minA[i] < P:
            continue
        if maxA[i] > R:
            continue
        if maxA[i] - minA[i] > R - P:
            continue
        if minA[i] == P and maxA[i] == R:
            res += 1
            continue
        if minA[i] == P:
            if maxA[i] == Q:
                res += 1
            continue
        if maxA[i] == R:
            if minA[i] == Q:
                res += 1
            continue
        if minA[i] == Q:
            if maxA[i] == R:
                res += 1
            continue
        if maxA[i] - minA[i] == Q - P:
            res += 1
    if res == 0:
        print('No')
    else:
        print('Yes')
solve()
