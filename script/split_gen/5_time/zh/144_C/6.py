def solve(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        tmp = int(n ** 0.5)
        if tmp ** 2 == n:
            return 2 * tmp - 2
        elif n - tmp ** 2 <= tmp:
            return 2 * tmp - 1
        else:
            return 2 * tmp
n = int(input())
print(solve(n))
