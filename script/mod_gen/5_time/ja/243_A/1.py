def solve():
    v, a, b, c = map(int, input().split())
    while True:
        if v - a < 0:
            return "F"
        else:
            v -= a
        if v - b < 0:
            return "M"
        else:
            v -= b
        if v - c < 0:
            return "T"
        else:
            v -= c

if __name__ == '__main__':
    solve()