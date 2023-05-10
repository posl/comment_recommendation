def solve():
    x, y = map(int, input().split())
    print(0 if x >= y else (y - x + 9) // 10)

if __name__ == '__main__':
    solve()