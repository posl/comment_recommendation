def main():
    N = int(input())
    if N < 250:
        print(0)
        return
    primes = []
    for i in range(2, N+1):
        if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
            primes.append(i)
    cnt = 0
    for i in primes:
        if i * (2**3) > N:
            break
        for j in range(2, N+1):
            if i * (j**3) > N:
                break
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()