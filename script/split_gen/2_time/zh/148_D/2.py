def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N)
    # print(A)
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    if ans == N:
        ans = 0
    elif ans == N - 1:
        ans = 1
    else:
        ans = N - ans
    print(ans)
