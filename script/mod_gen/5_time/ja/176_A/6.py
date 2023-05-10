def solve():
    n, x, t = map(int, input().split())
    if n % x == 0:
        return n // x * t
    else:
        return (n // x + 1) * t
print(solve())

if __name__ == '__main__':
    solve()