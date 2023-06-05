def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * n
    ans[0] = 0
    for i in range(1, n):
        if A[i] > A[i - 1]:
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1]
    for i in range(n):
        print(ans[i])
    return 0
