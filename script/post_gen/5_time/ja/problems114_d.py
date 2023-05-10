Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    # 素因数分解
    primes = []
    for i in range(2, n + 1):
        for j in range(2, i + 1):
            while i % j == 0:
                primes.append(j)
                i //= j
    # 75の約数を作る
    divs = [1]
    for p in primes:
        divs2 = divs[:]
        for d in divs2:
            divs.append(d * p)
    # 75の約数のうち、n!の約数の個数を数える
    ans = 0
    for d in divs:
        if d == 1:
            continue
        t = n
        while t % d == 0:
            ans += 1
            t //= d
    print(ans)

=======
Suggestion 2

def prime_factorize(n):
    # 素因数分解
    # 素因数とその個数のタプルのリストを返す
    # 素因数分解した結果を素因数とその個数のタプルのリストで返す
    # 例: 24 → [(2, 3), (3, 1)]
    # 例:  2 → [(2, 1)]
    # 例:  1 → []
    # 例:  0 → []
    if n <= 1:
        return []
    else:
        return [(d, e) for d, e in zip(*factorize(n))]

=======
Suggestion 3

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
n = int(input())
d = {}
for i in range(1, n + 1):
    for j in prime_factorize(i):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
a = 0
b = 0
c = 0
d = 0
e = 0
for i in d.values():
    if i >= 74:
        a += 1
    if i >= 24:
        b += 1
    if i >= 14:
        c += 1
    if i >= 4:
        d += 1
    if i >= 2:
        e += 1
print(a + b * (e - 1) + c * (d - 1) + d * (d - 1) * (e - 2) // 2)

=======
Suggestion 4

def calc_divisor(n):
    # 約数を格納するリスト
    divisors = []
    # 1 から n までの数で n を割った時に余りが 0 になるものを調べる
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            # 見つかった約数をリストに格納
            divisors.append(i)
            # n と割った数が同じでなければ n を割った商も約数になる
            if n // i != i:
                divisors.append(n//i)
    # 約数のリストをソートして出力
    divisors.sort()
    return divisors

=======
Suggestion 5

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1)+1)):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

=======
Suggestion 6

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

=======
Suggestion 7

def count_divisor(n):
    count = 0
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            n //= i
            count += 1
    if n != 1:
        count += 1
    return count

n = int(input())
ans = 0
divisors = [0 for _ in range(n+1)]
for i in range(2, n+1):
    divisors[i] = count_divisor(i)
for i in range(2, n+1):
    if divisors[i] >= 74:
        ans += 1
for i in range(2, n+1):
    for j in range(i+1, n+1):
        if divisors[i] >= 2 and divisors[j] >= 24:
            ans += 1
        if divisors[i] >= 4 and divisors[j] >= 14:
            ans += 1
        if divisors[i] >= 14 and divisors[j] >= 4:
            ans += 1
        if divisors[i] >= 24 and divisors[j] >= 2:
            ans += 1
print(ans)

=======
Suggestion 8

def prime_factorize(n):
    # 素因数分解
    # 戻り値: [[素因数, 指数], ...]
    # 計算量: O(√n)
    res = []
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            ex = 0
            while n%i==0:
                ex += 1
                n //= i
            res.append([i, ex])
    if n!=1:
        res.append([n, 1])
    return res

n = int(input())
pf = prime_factorize(n)

=======
Suggestion 9

def prime_factorize(n):
    # 素因数分解
    # 素因数を要素とするリストを返す
    # 例: 12 -> [2, 2, 3]
    # 計算量: O(√n)
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

n = int(input())

=======
Suggestion 10

def prime_factorize(n):
    from math import sqrt
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    f = 3
    while f <= sqrt(n):
        if n % f == 0:
            prime_factors.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_factors.append(n)
    return prime_factors

n = int(input())
d = {}
for i in range(1,n+1):
    for j in prime_factorize(i):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
cnt = 0
for i in d:
    if d[i] >= 74:
        cnt += 1
    for j in d:
        if i != j and d[i] >= 24 and d[j] >= 2:
            cnt += 1
        if i != j and d[i] >= 14 and d[j] >= 4:
            cnt += 1
        if i != j and d[i] >= 4 and d[j] >= 4 and i < j:
            cnt += 1
        for k in d:
            if i != j and j != k and k != i and d[i] >= 2 and d[j] >= 4 and d[k] >= 4:
                cnt += 1
print(cnt)
