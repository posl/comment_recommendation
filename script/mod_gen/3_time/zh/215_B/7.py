def solve(n):
    k = 0
    while 2 ** k <= n:
        k += 1
    return k - 1
print(solve(int(input())))
