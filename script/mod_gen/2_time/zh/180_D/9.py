def solve(x, y, a, b):
    exp = 0
    while x * a <= x + b and x * a < y:
        x *= a
        exp += 1
    exp += (y - 1 - x) // b
    return exp
x, y, a, b = map(int, input().split())
print(solve(x, y, a, b))
