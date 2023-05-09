def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        if A[i] < X:
            cnt += 1
        else:
            break
    if K >= cnt:
        print(0)
    else:
        print(sum(A[:N - K]))
