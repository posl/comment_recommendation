def count_divisors(n):
    # 1 is always a divisor
    count = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    return count
