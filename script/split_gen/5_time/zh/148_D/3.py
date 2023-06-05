def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        print(-1)
        exit()
    ans = 0
    for i in range(N - 1):
        if A[i + 1] - A[i] > 1:
            print(-1)
            exit()
        elif A[i + 1] - A[i] == 1:
            ans += 1
        else:
            ans += A[i]
    print(ans + A[-1])
solve()
