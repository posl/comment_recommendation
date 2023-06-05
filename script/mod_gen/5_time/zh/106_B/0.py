def count_divisors(n):
    if n == 1:
        return 1
    count = 2
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            count += 1
    return count

if __name__ == '__main__':
    count_divisors()