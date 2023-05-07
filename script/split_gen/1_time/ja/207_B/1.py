def solve():
    A, B, C, D = map(int, input().split())
    if B >= C * D:
        print(-1)
        return
    ans = 0
    while A > C * D:
        A -= B
        ans += 1
    print(ans)
    return
