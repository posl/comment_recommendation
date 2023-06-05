def count_odd(n, a):
    count = 0
    for i in range(n):
        if a[i] % 2 != 0:
            count += 1
    return count
