def get_divisor_count(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count
