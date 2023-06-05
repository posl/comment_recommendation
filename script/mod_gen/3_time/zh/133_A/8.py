def solve():
    n, a, b = map(int, input().split())
    print(min(n*a, b))

if __name__ == '__main__':
    solve()