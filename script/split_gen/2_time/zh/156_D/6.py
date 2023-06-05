def calc_sum(x, n):
    sum = 0
    for i in range(n):
        sum += (x - i) ** 2
    return sum
