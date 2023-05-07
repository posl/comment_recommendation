def main():
    #入力
    N, M = map(int, input().split())
    #素因数分解
    def prime_factorize(n):
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
    #出力
    print(len(set(prime_factorize(M)))**N % (10**9+7))

if __name__ == '__main__':
    main()