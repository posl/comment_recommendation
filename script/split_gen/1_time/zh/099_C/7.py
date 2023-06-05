def get_min_count(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    min_count = n
    for i in range(1, n):
        if i**2 > n:
            break
        min_count = min(min_count, get_min_count(n - i**2) + 1)
    return min_count
