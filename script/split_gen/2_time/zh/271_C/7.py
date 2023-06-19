def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] <= i + 1:
            ans = i + 1
    print(ans)
