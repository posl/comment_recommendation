def main():
    N, M = map(int, input().split())
    # prime factorization
    prime_factors = []
    for i in range(2, int(M ** 0.5) + 1):
        if M % i == 0:
            tmp = 0
            while M % i == 0:
                M //= i
                tmp += 1
            prime_factors.append(tmp)
    if M != 1:
        prime_factors.append(1)
    
    # combination
    comb = 1
    mod = 10 ** 9 + 7
    for i in prime_factors:
        comb = comb * (i + N) * pow(i, mod - 2, mod) % mod
    print(comb)

if __name__ == '__main__':
    main()