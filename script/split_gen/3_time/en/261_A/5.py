def paint():
    L1, R1, L2, R2 = map(int, input().split())
    if L1 <= L2 <= R1 or L2 <= L1 <= R2:
        print(min(R1, R2) - max(L1, L2))
    else:
        print(0)
