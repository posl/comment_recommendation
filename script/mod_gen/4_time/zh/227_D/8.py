def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    print(A)
    i = 0
    j = 0
    cnt = 0
    while j < N:
        if A[j] - A[i] >= K:
            i += 1
            cnt += 1
        j += 1
    print(cnt)
solve()
