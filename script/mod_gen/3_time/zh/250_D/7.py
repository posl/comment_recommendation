def get_factors(num):
    factors = []
    for i in range(2, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    get_factors()