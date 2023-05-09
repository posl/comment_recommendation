def solve():
    a, b = map(int, input().split())
    print(max(0, b - a + 1))
solve()

if __name__ == '__main__':
    solve()