def solve(x, y):
    for i in range(x + 1):
        if (i * 2 + (x - i) * 4) == y:
            return True
    return False
x, y = map(int, input().split())

if __name__ == '__main__':
    solve()