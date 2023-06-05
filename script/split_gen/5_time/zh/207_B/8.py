def solve():
    A, B, C, D = map(int, input().split())
    if A < B:
        print(-1)
        return
    if D == 1:
        print(0)
        return
    if B >= C * D:
        print(-1)
        return
    ans = 0
    while A > 0:
        if A <= B:
            print(ans)
            return
        A -= B
        A += C
        ans += 1
    print(ans)
    return
