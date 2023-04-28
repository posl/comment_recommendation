Synthesizing 10/10 solutions (Duplicates hidden)

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
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = prime_factorize(n)
    p = a[0]
    q = 1
    for i in range(1,len(a)):
        if a[i] == p:
            q *= p
            p = a[i+1]
            break
    q *= p
    print(p,q)

=======
Suggestion 2

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
    p = prime_factorize(N)
    if len(p) == 3:
        print(p[0],p[1])
    else:
        print(p[0],p[0]**2)

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

t=int(input())
for i in range(t):
    n=int(input())
    a=prime_factorize(n)
    print(a[0],a[1])

=======
Suggestion 4

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

t = int(input())
n = [0] * t
for i in range(t):
    n[i] = int(input())
for i in range(t):
    a = prime_factorize(n[i])
    print(a[0], a[1])

=======
Suggestion 5

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
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
T = int(input())
for i in range(T):
    N = int(input())
    arr = factorization(N)
    print(arr[0][0],arr[1][0])

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+2):
        if n%i == 0:
            return False
    return True

=======
Suggestion 7

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        for j in range(2, int(N**0.5)+1):
            if N % j == 0:
                if N % (j*j) == 0:
                    print(j, int(N/j/j))
                    break

=======
Suggestion 8

def get_prime_list(N):
    prime_list = [2]
    for i in range(3, N+1, 2):
        for j in range(3, i, 2):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list

=======
Suggestion 9

def get_prime_numbers(n):
    prime_numbers = []
    # 2からnまでの整数を素数判定する
    for i in range(2, n + 1):
        # 2からi-1までの整数で割り切れるかどうかを判定
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers
