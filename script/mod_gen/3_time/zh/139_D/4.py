def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 3
    if n % 2 == 0:
        return n * (n - 1) // 2
    else:
        return n * (n - 1) // 2 - 1
print(solve(int(input())))
