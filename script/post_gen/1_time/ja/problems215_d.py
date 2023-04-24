Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

=======
Suggestion 3

def gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 4

def get_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False
    return primes

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #gcd
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    #lcm
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    #lcm
    def lcm_list(A):
        return reduce(lcm, A)
    #lcm
    def lcm_list2(A):
        return functools.reduce(lcm, A)
    #gcd
    def gcd_list(A):
        return reduce(gcd, A)
    #gcd
    def gcd_list2(A):
        return functools.reduce(gcd, A)
    #最小公倍数
    lcm_A = lcm_list2(A)
    #最大公約数
    gcd_A = gcd_list2(A)
    #最小公倍数の約数を列挙
    div_lcm_A = []
    for i in range(1, int(lcm_A ** 0.5) + 1):
        if lcm_A % i == 0:
            div_lcm_A.append(i)
            if i != lcm_A // i:
                div_lcm_A.append(lcm_A // i)
    #最大公約数の約数を列挙
    div_gcd_A = []
    for i in range(1, int(gcd_A ** 0.5) + 1):
        if gcd_A % i == 0:
            div_gcd_A.append(i)
            if i != gcd_A // i:
                div_gcd_A.append(gcd_A // i)
    #最小公倍数の約数のうち、最大公約数の約数でないものを列挙
    div_lcm_A2 = []
    for i in div_lcm_A:
        if i not in div_gcd_A:
            div_lcm_A2.append(i)
    #最小公倍数の約数のうち、最大公約数の約数でないものを列挙
    div_lcm_A3 = []
    for i in div_lcm_A2:
        if i <= M:
            div_lcm

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    import math
    def gcd(a,b):
        if a<b:
            a,b = b,a
        while b!=0:
            a,b = b,a%b
        return a
    def lcm(a,b):
        return a*b//gcd(a,b)
    G = A[0]
    for i in range(1,N):
        G = gcd(G,A[i])
    if M%G!=0:
        print(0)
        return
    M = M//G
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(1,int(math.sqrt(M))+1):
        if M%i==0:
            d[i] = 1
            d[M//i] = 1
    d = sorted(d.items())
    ans = []
    for i in range(len(d)):
        if d[i][1]==1:
            ans.append(d[i][0]*G)
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(A[0])
    #print(A[N-1])
    #print(A[N-1]//A[0])
    #print(A[N-1]%A[0])
    #print(A[N-1]//A[0] + 1)
    #print(A[N-1]//A[0] - 1)
    #print(A[N-1]//A[0] - 2)
    #print(A[N-1]//A[0] - 3)
    #print(A[N-1]//A[0] - 4)
    #print(A[N-1]//A[0] - 5)
    #print(A[N-1]//A[0] - 6)
    #print(A[N-1]//A[0] - 7)
    #print(A[N-1]//A[0] - 8)
    #print(A[N-1]//A[0] - 9)
    #print(A[N-1]//A[0] - 10)
    #print(A[N-1]//A[0] - 11)
    #print(A[N-1]//A[0] - 12)
    #print(A[N-1]//A[0] - 13)
    #print(A[N-1]//A[0] - 14)
    #print(A[N-1]//A[0] - 15)
    #print(A[N-1]//A[0] - 16)
    #print(A[N-1]//A[0] - 17)
    #print(A[N-1]//A[0] - 18)
    #print(A[N-1]//A[0] - 19)
    #print(A[N-1]//A[0] - 20)
    #print(A[N-1]//A[0] - 21)
    #print(A[N-1]//A[0] - 22)
    #print(A[N-1]//A[0] - 23)
    #print(A[N-1]//A[0] - 24)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(N, M)
    #print(A)
    #print(A[0])
    #print(A[-1])
    #print(A[0] == 1)
    #print(A[-1] == M)
    #print(A[0] == 1 and A[-1] == M)
    if A[0] == 1 and A[-1] == M:
        print(0)
        exit()
    #print(A)
    #p
