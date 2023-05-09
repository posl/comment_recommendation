def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = list(enumerate(A))
    A.sort(key=lambda x: x[1])
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[i] = N - 1
        else:
            ans[i] = ans[i - 1] - 1
    for i in range(N):
        ans[A[i][0]] = ans[i]
    for a in ans:
        print(a)
