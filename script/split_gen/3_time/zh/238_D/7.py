def bit_sum(x):
    sum = 0
    while x != 0:
        sum += x % 2
        x /= 2
    return sum
