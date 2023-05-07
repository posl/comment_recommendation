def solve(x, y):
    if x == 0 or y == 0:
        return 0
    elif x == 1 and y == 1:
        return 2
    elif x == 1 or y == 1:
        return max(x, y)
    else:
        return (solve(x - 1, y) + solve(x, y - 1)) % 1000000007
x, y = map(int, input().split())
print(solve(x, y))

if __name__ == '__main__':
    solve()