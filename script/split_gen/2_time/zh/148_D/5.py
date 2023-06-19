def solve():
    N = int(input())
    A = map(int, input().split())
    ans = 0
    for i, a in enumerate(A, 1):
        if i != a:
            ans += 1
    if ans == N:
        ans = -1
    print(ans)
