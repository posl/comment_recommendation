def solve():
    a, b = map(int, input().split())
    print((a * b**2)**0.5 - b)

if __name__ == '__main__':
    solve()