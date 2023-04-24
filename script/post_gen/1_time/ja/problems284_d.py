Synthesizing 10/10 solutions

=======
Suggestion 1

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

T = int(input())
for i in range(T):
    N = int(input())
    a = prime_factorize(N)
    p = a[0]
    q = N // (p ** 2)
    print(p, q)

=======
Suggestion 2

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

T = int(input())
for i in range(T):
    N = int(input())
    p = prime_factorization(N)
    print(p[0],p[-1])

=======
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            if is_prime(i) and is_prime(N//i):
                print(i, N//i)
                break

=======
Suggestion 4

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        p = 0
        q = 0
        for i in range(2, int(N**0.5)+1):
            if N % i == 0:
                p = i
                q = N // i
                break
        print(p, q)

=======
Suggestion 5

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        p = 0
        q = 0
        for j in range(2, int(N**0.5)+1):
            if N % j == 0:
                p = j
                q = N // (j**2)
                break
        print(p, q)

=======
Suggestion 6

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        p = 0
        q = 0
        for j in range(2, N):
            if N % j == 0:
                p = j
                N = N // j
                break
        for j in range(2, N):
            if N % j == 0:
                q = j
                N = N // j
                break
        print(p, q)

=======
Suggestion 7

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        for p in range(2, N):
            if N % p == 0:
                q = N // p ** 2
                break
        print(p, q)

=======
Suggestion 8

def main():
    T = int(input())
    N = [int(input()) for _ in range(T)]
    for i in range(T):
        p = 0
        q = 0
        for j in range(2, int(N[i] ** (1/2)) + 1):
            if N[i] % j == 0:
                p = j
                q = N[i] // j
                break
        print(p, q)

=======
Suggestion 9

def main():
    #入力
    T = int(input())
    N = [int(input()) for _ in range(T)]
    
    #処理
    #N=p^2q
    #p,qを求める
    #pは平方根をとる
    #qはNをpで割ったものの平方根をとる
    p = [int(N[i]**(1/2)) for i in range(T)]
    q = [int(N[i]/p[i]**2) for i in range(T)]
    
    #出力
    for i in range(T):
        print(p[i],q[i])

=======
Suggestion 10

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        #素数リストを作成
        prime_list = [2]
        for j in range(3, int(N**0.5)+1, 2):
            for k in prime_list:
                if j % k == 0:
                    break
            else:
                prime_list.append(j)
        #N=p^2qを満たす素数p,qを探す
        for p in prime_list:
            if N % p == 0:
                q = N // p
                if q % p == 0:
                    print(p, q // p)
                    break
