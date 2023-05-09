def solve():
    H,W = map(int, input().split())
    r,c = map(int, input().split())
    print(2 if r in (1,H) and c in (1,W) else 3 if r in (1,H) or c in (1,W) else 4)
solve()
