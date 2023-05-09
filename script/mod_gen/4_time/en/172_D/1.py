def f(x):
    divisors = 0
    for i in range(1, x+1):
        if x % i == 0:
            divisors += 1
    return divisors

if __name__ == '__main__':
    f()