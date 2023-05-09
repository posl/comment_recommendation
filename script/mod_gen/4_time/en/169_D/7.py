def get_primes(max_num):
    # get primes under max_num
    primes = [2, 3]
    for i in range(5, max_num, 2):
        for j in range(3, int(i**0.5)+1, 2):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

if __name__ == '__main__':
    get_primes()