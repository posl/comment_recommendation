def solve(x, y):
    if x < 0 or y < 0:
        return 0
    if x == 0 and y == 0:
        return 1
    return (solve(x - 1, y - 2) + solve(x - 2, y - 1)) % 1000000007
x, y = map(int, input().split())
print(solve(x, y))
