def solve():
    n,r = map(int, raw_input().split())
    if n >= 10:
        print r
    else:
        print r + 100 * (10 - n)
