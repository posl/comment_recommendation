def get_sum(n, a, b):
    # count the number of integers that are multiples of a or b
    cnt = n // a + n // b - n // lcm(a, b)
    # count the sum of integers that are multiples of a or b
    sum = (1 + n) * n // 2 - ((a + a * (cnt - 1)) * cnt // 2 + (b + b * (cnt - 1)) * cnt // 2 - (lcm(a, b) + lcm(a, b) * (cnt - 1)) * cnt // 2)
    return sum
