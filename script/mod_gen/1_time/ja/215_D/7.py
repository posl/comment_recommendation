def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # M 以下の素数を列挙
    is_prime = [True] * (M + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(M ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, M + 1, i):
                is_prime[j] = False
    primes = [i for i in range(M + 1) if is_prime[i]]
    # 素因数分解
    factor = [[] for _ in range(M + 1)]
    for p in primes:
        for i in range(p, M + 1, p):
            factor[i].append(p)
    # 約数の個数
    cnt = [1] * (M + 1)
    for a in A:
        for p in factor[a]:
            cnt[p] += 1
    # 答え
    ans = []
    for i in range(1, M + 1):
        f = True
        for p in factor[i]:
            if cnt[p] > 1:
                f = False
                break
        if f:
            ans.append(i)
    print(len(ans))
    print(*ans, sep='
')

if __name__ == '__main__':
    main()