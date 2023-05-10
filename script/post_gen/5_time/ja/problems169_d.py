Synthesizing 10/10 solutions

=======
Suggestion 1

def prime_factorize(n):
    # 素因数分解
    # 素因数を格納するリスト
    f = []
    # 2から√n以下の整数で割っていく
    while n % 2 == 0:
        f.append(2)
        n //= 2
    i = 3
    while i*i <= n:
        if n % i == 0:
            f.append(i)
            n //= i
        else:
            i += 2
    if n != 1:
        f.append(n)
    return f

n = int(input())
f = prime_factorize(n)
f.sort()
f = list(set(f))
ans = 0
for i in range(len(f)):
    if n % f[i] == 0:
        ans += 1
        n //= f[i]
print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    n2 = n
    ans = 0
    for i in range(2, int(n**0.5)+1):
        if n2 % i == 0:
            ans += 1
            n2 //= i
        while n2 % i == 0:
            n2 //= i
    if n2 != 1:
        ans += 1
    print(ans)

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
    
N = int(input())
a = prime_factorize(N)
a = list(set(a))
a.sort()
a.reverse()
ans = 0
for i in range(len(a)):
    tmp = N
    while tmp % a[i] == 0:
        tmp //= a[i]
    N = tmp
    ans += 1
print(ans)

=======
Suggestion 4

def factorize(n):
    fct = []
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

n = int(input())
f = factorize(n)
ans = 0
for a, b in f:
    i = 1
    while b >= i:
        b -= i
        i += 1
        ans += 1
print(ans)

=======
Suggestion 5

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0: 
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

N = int(input())
ans = 0
divisors = make_divisors(N)
divisors.sort(reverse=True)
for i in divisors:
    if i == 1:
        break
    n = N
    while n % i == 0:
        n = n // i
    if n % i == 1:
        ans += 1
print(ans)

=======
Suggestion 6

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

n=int(input())
f=factorization(n)
ans=0
for i in f:
    j=1
    while i[1]>=j:
        i[1]-=j
        j+=1
        ans+=1
print(ans)

=======
Suggestion 7

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

N = int(input())
prime_list = prime_factorize(N)
prime_set = set(prime_list)
ans = 0
for i in prime_set:
    prime_list.count(i)
    if prime_list.count(i) == 1:
        ans += 1
    elif prime_list.count(i) == 2:
        ans += 1
    else:
        ans += int((prime_list.count(i)+2)/2)
print(ans)

=======
Suggestion 8

def prime_factorize(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime_factors.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_factors.append(n)
    return prime_factors

N = int(input())
prime_factors = prime_factorize(N)
prime_factors.sort()

ans = 0

=======
Suggestion 9

def prime_factorize(n):
    prime_factor = []
    while n % 2 == 0:
        prime_factor.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime_factor.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_factor.append(n)
    return prime_factor

n = int(input())
prime_list = prime_factorize(n)
prime_set = set(prime_list)
ans = 0
for p in prime_set:
    e = prime_list.count(p)
    tmp = 1
    while e >= tmp:
        e -= tmp
        tmp += 1
        ans += 1
print(ans)

=======
Suggestion 10

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True

n = int(input())
ans = 0
for i in range(2, int(n**0.5)+1):
    if is_prime(i) and n%i == 0:
        while n%i == 0:
            n //= i
            ans += 1
