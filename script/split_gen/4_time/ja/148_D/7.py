def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = 0
    for i in range(1, N + 1):
        if A[i] != i:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(ans)
