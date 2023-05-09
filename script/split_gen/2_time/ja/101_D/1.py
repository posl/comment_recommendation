def digit_sum(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum
