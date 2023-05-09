def divisorCount(n):
    if n == 1:
        return 1
    count = 2
    i = 2
    while i*i < n:
        if n % i == 0:
            count += 2
        i += 1
    if i*i == n:
        count += 1
    return count
