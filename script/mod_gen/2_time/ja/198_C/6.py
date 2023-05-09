def solve():
    import sys
    readline = sys.stdin.readline
    r, x, y = map(int, readline().split())
    if x**2 + y**2 < r**2:
        print(2)
    else:
        print((x**2 + y**2 + r**2 - 1)//(r**2))

if __name__ == '__main__':
    solve()