def get_divisor_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * f(i)
    return sum
