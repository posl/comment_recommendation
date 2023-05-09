def main():
    n, m = map(int, input().split())
    mod = 10**9 + 7
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
    #素因数の個数
    def prime_factor_cnt(n):
        a = prime_factorize(n)
        cnt = 1
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                cnt += 1
            else:
                cnt *= 2
        return cnt
    #2のべき乗の数
    def cnt_2(n):
        cnt = 0
        while n % 2 == 0:
            cnt += 1
            n //= 2
        return cnt
    #2のべき乗の数の総和
    def sum_2(n):
        cnt = 0
        while n % 2 == 0:
            cnt += 1
            n //= 2
        return cnt + sum_2(n)
    #2のべき乗の数の総和
    def sum_2(n):
        cnt = 0
        while n % 2 == 0:
            cnt += 1
            n //= 2
        return cnt + sum_2(n)
    #2のべき乗の数の総和
    def sum_2(n):
        cnt = 0
        while n % 2 == 0:
            cnt += 1
            n //= 2
        return cnt + sum_2(n)
    #2のべき乗の数の総和
    def sum_2(n):
        cnt = 0
        while n % 2 == 0:
            cnt += 1
            n //= 2
        return cnt + sum_2(n)
    #2のべき乗の

if __name__ == '__main__':
    main()