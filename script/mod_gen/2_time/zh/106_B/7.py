def get_divisors(n):
    divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors += 1
    return divisors

if __name__ == '__main__':
    get_divisors()