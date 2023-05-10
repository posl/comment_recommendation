def solve():
    A, B, C = map(int, input().split())
    print((A+B+C) * (100 - A - B - C) / (A+B+C))

if __name__ == '__main__':
    solve()