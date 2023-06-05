def solve(n, x, ab):
    # n: number of coins
    # x: target
    # ab: list of (a, b)
    # return: True/False
    # print(n, x, ab)
    if n == 0:
        return False
    a, b = ab[0]
    if a * b == x:
        return True
    if a * b > x:
        return solve(n - 1, x, ab[1:])
    else:
        return solve(n - 1, x - a * b, ab[1:])

if __name__ == '__main__':
    solve()