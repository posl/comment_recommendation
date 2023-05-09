def main():
    N = int(input())
    primes = get_primes(N)
    k = 0
    for p in primes:
        for q in primes:
            if p*q**3 <= N:
                k += 1
            else:
                break
    print(k)

if __name__ == '__main__':
    main()