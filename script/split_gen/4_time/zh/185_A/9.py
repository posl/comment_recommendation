def solve():
    a1, a2, a3, a4 = map(int, input().split())
    res = 0
    if a1 == 100:
        res += 1
    if a2 == 100:
        res += 1
    if a3 == 100:
        res += 1
    if a4 == 100:
        res += 1
    print(res)
