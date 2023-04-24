Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = [[] for _ in range(N)]
    for i in range(N):
        L = list(map(int, input().split()))
        A[i] = L[1:]
    ans = 0
    for i in range(1, 2**N):
        tmp = 1
        for j in range(N):
            if (i >> j) & 1:
                tmp *= A[j][0]
            else:
                tmp *= A[j][1]
        if tmp == X:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    L = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        L[i], *A[i] = map(int, input().split())
    #print(L, A)
    ans = 0
    for i in range(2**N):
        p = 1
        for j in range(N):
            if (i >> j) & 1:
                p *= A[j][0]
            else:
                p *= A[j][-1]
        if p <= X:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, 1 << N):
        p = 1
        for j in range(N):
            if i >> j & 1:
                p *= L[j][1 + (i >> j & 1)]
        if X % p == 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 1 << N):
        flag = True
        mul = 1
        for j in range(N):
            if (1 << j) & i:
                mul *= L[j][1 + (i >> j) % L[j][0] - 1]
                if mul > X:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(2 ** N):
        tmp = 1
        for j in range(N):
            if ((i >> j) & 1):
                tmp *= L[j][(i >> j) & 1]
        if tmp == X:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 1<<N):
        cnt = 0
        num = 1
        for j in range(N):
            if i>>j & 1:
                cnt += 1
                num *= L[j][cnt]
        if num == X:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))
        L[-1].pop(0)
    ans = 0
    for i in range(2**N):
        s = 1
        for j in range(N):
            if (i>>j)&1:
                s *= L[j][(i>>j)&1]
        if s == X:
            ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines

    N, X = map(int, readline().split())
    *A, = map(int, read().split())

    from collections import defaultdict
    from math import gcd

    def prime_factorize(n):
        fct = defaultdict(int)
        for i in range(2, int(n**0.5)+1):
            while n % i == 0:
                n //= i
                fct[i] += 1
        if n > 1:
            fct[n] += 1
        return fct

    fct = prime_factorize(X)
    if not fct:
        print(0)
        return

    # 1つずつの素因数を含む組み合わせの数
    def count(fct, A):
        res = 1
        for p, e in fct.items():
            cnt = 0
            for a in A:
                while a % p == 0:
                    a //= p
                    cnt += 1
            res *= cnt + 1
        return res

    cnt = count(fct, A)
    # 2つ以上の素因数を含む組み合わせの数
    for p, e in fct.items():
        if e == 1:
            continue
        fct2 = fct.copy()
        fct2[p] = 1
        cnt -= count(fct2, A)
    print(cnt)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for i in range(N)]
    #print(N, X)
    #print(L)

    ans = 0
    for i in range(2**N):
        s = 1
        for j in range(N):
            if ((i >> j) & 1):
                s *= L[j][1]
            else:
                s *= L[j][2]
        if s == X:
            ans += 1

    print(ans)

=======
Suggestion 10

def get_primes(n): #n以下の素数を返す
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = [i+1 for i in range(1, n, 2)]
    m = int(n ** 0.5)
    half = (n+1)//2 - 1
    i = 0
    m2 = 3
    while m2 <= m:
        if s[i]:
            j = (m2*m2-3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m2
        i = i + 1
        m2 = 2*i + 3
    return [2] + [el for el in s if el]
