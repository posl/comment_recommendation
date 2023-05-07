def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    # 素因数分解
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
    # 素因数の集合
    prime_set = set()
    for a in A:
        for p in prime_factorize(a):
            prime_set.add(p)
    # 約数の集合
    divisor_set = set()
    for p in prime_set:
        d = p
        while d <= M:
            divisor_set.add(d)
            d += p
    # 答え
    answer = len(divisor_set)
    print(answer)
    for d in sorted(divisor_set):
        print(d)
