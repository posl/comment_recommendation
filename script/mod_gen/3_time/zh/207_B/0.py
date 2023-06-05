def solve():
    A, B, C, D = map(int, input().split())
    if A < B:
        print(-1)
        return
    if D == 1:
        print(0)
        return
    # D > 1
    if B >= C * D:
        print(-1)
        return
    # B < C * D
    t1 = (A - B) // (C * D - B)
    t2 = t1 + 1
    if t1 * C * D + B >= A:
        print(t1)
    else:
        print(t2)

if __name__ == '__main__':
    solve()