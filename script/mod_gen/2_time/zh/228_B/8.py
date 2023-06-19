def solution():
    N,X = map(int, input().split())
    A = list(map(int, input().split()))
    A[X-1] = 0
    ans = 1
    for i in range(N):
        if A[i] != 0:
            ans += 1
            A[A[i]-1] = 0
    print(ans)
solution()
