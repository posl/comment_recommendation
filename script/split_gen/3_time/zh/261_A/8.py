def solve():
    l1, r1, l2, r2 = map(int, input().split())
    if r1 <= l2 or r2 <= l1:
        print(0)
    else:
        print(min(r1, r2) - max(l1, l2))
