def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] > ans + 1:
            break
        else:
            ans += A[i]
    print(ans + 1)
