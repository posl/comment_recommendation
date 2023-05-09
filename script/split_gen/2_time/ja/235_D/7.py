def solve(a, n):
    if n == 1:
        return 0
    elif n % a == 0:
        return solve(a, n // a) + 1
    else:
        num = n % 10
        if num == 1:
            return solve(a, n // 10) + 1
        elif num == 0:
            return -1
        else:
            return solve(a, n - num) + 1
