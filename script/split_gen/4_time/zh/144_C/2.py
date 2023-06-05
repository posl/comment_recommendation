def find_min_steps(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    for i in range(2, n):
        if n % i == 0:
            return find_min_steps(n / i) + i - 1
    return n - 1
