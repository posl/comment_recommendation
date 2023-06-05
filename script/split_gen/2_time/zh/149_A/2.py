def solve():
    N = int(input())
    a = [int(i) for i in input().split()]
    if a[0] != 1:
        print(-1)
        return
    for i in range(1, N):
        if a[i] - a[i-1] > 1:
            print(-1)
            return
    ans = N
    for i in range(N-1, -1, -1):
        if a[i] == ans:
            ans -= 1
    print(ans)
