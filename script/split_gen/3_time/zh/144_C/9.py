def solve(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return n // i - 1
            i += 1
        return n - 1
