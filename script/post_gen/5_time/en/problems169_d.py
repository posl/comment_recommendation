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

N = int(input())
pf = prime_factorize(N)
pf_set = set(pf)
ans = 0

for x in pf_set:
    i = 0
    while True:
        if x**(i+1) > N:
            ans = max(ans, i)
            break
        else:
            i += 1

print(ans)

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

N = int(input())
p = prime_factorize(N)
p.sort()
ans = 0
count = 0
for i in range(len(p)):
    if p[i] == p[i-1]:
        count += 1
    else:
        count = 1
    if count == 1:
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
A = prime_factorize(N)
B = list(set(A))
C = list(set(A))
D = list(set(A))
E = []
for i in range(len(B)):
    for j in range(len(C)):
        for k in range(len(D)):
            E.append(B[i]*C[j]*D[k])
F = list(set(E))
G = []
for i in range(len(F)):
    G.append(N//F[i])
H = list(set(G))
print(len(H)-1)

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
for i in range(len(f)):
    c = 0
    while f[i][1] >= c:
        f[i] = (f[i][0], f[i][1] - c)
        c += 1
        ans += 1
print(ans - 1)

=======
Suggestion 5

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = int(input())
l = prime_factors(n)
l = list(set(l))
l.sort()
#print(l)
ans = 0
for i in l:
    num = 0
    while n % i == 0:
        n = n // i
        num += 1
    #print(num)
    for j in range(1, num+1):
        num -= j
        if num >= 0:
            ans += 1
        else:
            break
print(ans)

=======
Suggestion 6

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = int(input())

factors = prime_factors(n)
factors = list(set(factors))

count = 0
for i in factors:
    tmp = n
    while tmp % i == 0:
        count += 1
        tmp /= i

print(count)

=======
Suggestion 7

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

=======
Suggestion 8

def factorize(n):
    fct = []
    b,e = 2,0
    while b*b <= n:
        while n % b == 0:
            n = n//b
            e = e+1
        if e > 0:
            fct.append((b,e))
        b,e = b+1,0
    if n > 1:
        fct.append((n,1))
    return fct

n = int(input())
fct = factorize(n)
ans = 0
for b,e in fct:
    x = 1
    while e >= x:
        e -= x
        ans += 1
        x += 1
print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N ** 0.5) + 1):
        while N % i == 0:
            ans += 1
            N //= i
    if N > 1:
        ans += 1
    print(ans)

=======
Suggestion 10

def main():
    # Get input here
    N = int(input())

    # Calculate result here
    result = 0
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            result += 1
            N = N // i
            while N % i == 0:
                N = N // i
    if N != 1:
        result += 1

    # Print output here
    print(result)

main()
