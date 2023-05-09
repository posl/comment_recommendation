def get_primes(num):
    primes = []
    div = 2
    while num > 1:
        if num % div == 0:
            primes.append(div)
            num //= div
        else:
            div += 1
    return primes

if __name__ == '__main__':
    get_primes()