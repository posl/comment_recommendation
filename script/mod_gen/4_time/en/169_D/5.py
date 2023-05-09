def main():
    N = int(input())
    # 素因数分解
    def prime_factorization(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a
    factors = prime_factorization(N)
    print(len(set(factors)))

if __name__ == '__main__':
    main()