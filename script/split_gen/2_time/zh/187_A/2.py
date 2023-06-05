def sum_of_absolute_differences(n, a):
    a.sort()
    sum = 0
    for i in range(n):
        sum += a[i] * (i - (n - i - 1))
    return sum
