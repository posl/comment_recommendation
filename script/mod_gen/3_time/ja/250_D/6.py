def main():
    N = int(input())
    if N < 250:
        print(0)
        return
    primes = [2]
    for i in range(3, N, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
    count = 0
    for p in primes:
        if p >= N:
            break
        q = 1
        while p * (q+1)**3 <= N:
            q += 1
        count += q
    print(count)

if __name__ == '__main__':
    main()