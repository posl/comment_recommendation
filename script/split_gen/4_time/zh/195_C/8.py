def solve(n):
    if n <= 999:
        return 0
    elif n <= 999999:
        return n - 999
    elif n <= 999999999:
        return 2 * (n - 999999) + 999000
    elif n <= 999999999999:
        return 3 * (n - 999999999) + 999000000
    elif n <= 999999999999999:
        return 4 * (n - 999999999999) + 999000000000
    else:
        return 5 * (n - 999999999999999) + 999000000000000
n = int(input())
print(solve(n))
