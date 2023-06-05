def get_arithmetic_series_num(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i % 2 == 1:
                count += 1
            if i != n // i and (n // i) % 2 == 1:
                count += 1
    return count
