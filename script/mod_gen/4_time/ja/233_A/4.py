def solve():
    x, y = map(int, input().split())
    return max(0, (y - x) // 10)
print(solve())

if __name__ == '__main__':
    solve()