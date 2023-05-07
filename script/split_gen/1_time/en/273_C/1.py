def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        if i > 0 and A[i] == A[i - 1]:
            ans[i] = ans[i - 1]
        else:
            ans[i] = N - i - 1
    for i in ans:
        print(i)
    return 0
