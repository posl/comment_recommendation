def main():
    n = int(input())
    primes = [2]
    for i in range(3, int(n**0.5)+1, 2):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    count = 0
    for i in primes:
        while n % i == 0:
            n //= i
            count += 1
    if n != 1:
        count += 1
    print(count)

if __name__ == '__main__':
    main()