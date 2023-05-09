def problem207_b():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
        return
    if B * C >= A:
        print(1)
        return
    print((A - B * C - 1) // (B * D - B * C) + 1)
