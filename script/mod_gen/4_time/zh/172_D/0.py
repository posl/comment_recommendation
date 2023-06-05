def divisors(x):
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    divisors()