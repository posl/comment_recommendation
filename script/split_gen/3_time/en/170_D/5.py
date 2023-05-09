def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
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
    # 素因数のリストを作成
    prime = []
    for i in range(N):
        prime += prime_factorize(A[i])
    prime = list(set(prime))
    # 素因数の個数をカウント
    count = {}
    for i in range(len(prime)):
        count[prime[i]] = 0
    for i in range(N):
        for j in range(len(prime)):
            if A[i] % prime[j] == 0:
                count[prime[j]] += 1
    # 素因数の個数が1であるものを数える
    ans = 0
    for i in range(len(prime)):
        if count[prime[i]] == 1:
            ans += 1
    print(ans)
