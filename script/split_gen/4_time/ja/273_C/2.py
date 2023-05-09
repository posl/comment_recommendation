def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans[i] = ans[i-1] + 1
        else:
            ans[i] = ans[i-1]
    for i in range(N):
        print(ans[i]-1)
    return 0
