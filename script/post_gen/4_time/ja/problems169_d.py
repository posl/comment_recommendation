Synthesizing 10/10 solutions

=======
Suggestion 1

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

n = int(input())
f = factorization(n)
ans = 0
for x in f:
    e = x[1]
    i = 1
    while e >= i:
        ans += 1
        e -= i
        i += 1
print(ans)

=======
Suggestion 2

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

n = int(input())
f = factorization(n)
ans = 0
for i in f:
    for j in range(1, i[1]+1):
        i[1] -= j
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

N=int(input())
list=prime_factorize(N)
list.sort()
count=0
tmp=0
for i in range(len(list)):
    if list[i]!=tmp:
        tmp=list[i]
        count+=1
print(count)

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

N = int(input())
ans = 0
pf = prime_factorize(N)
for i in range(len(pf)):
    if i == 0:
        ans += 1
    elif pf[i] != pf[i-1]:
        ans += 1

print(ans)

=======
Suggestion 5

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
a = prime_factorize(n)
b = list(set(a))
c = []
for i in b:
    c.append(a.count(i))
ans = 0
for i in c:
    ans += (-1 + (2 * i - 1) ** 0.5) // 2
print(int(ans))

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

n = int(input())
ans = 0

=======
Suggestion 7

def prime_factorize(N):
    a = []
    while N % 2 == 0:
        a.append(2)
        N //= 2
    f = 3
    while f * f <= N:
        if N % f == 0:
            a.append(f)
            N //= f
        else:
            f += 2
    if N != 1:
        a.append(N)
    return a

N = int(input())
pf = prime_factorize(N)
pf_set = set(pf)
pf_len = len(pf_set)
pf_count = [pf.count(x) for x in pf_set]
pf_count.sort(reverse=True)
ans = 0
for i in range(len(pf_count)):
    c = pf_count[i]
    ans += int((-1+(1+8*c)**0.5)/2)
print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            cnt = 0
            while N % i == 0:
                cnt += 1
                N //= i
            for j in range(1, 100):
                if cnt >= j:
                    cnt -= j
                    ans += 1
                else:
                    break
    if N != 1:
        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    while N % 2 == 0:
        N //= 2
        ans += 1
    for i in range(3, int(N**0.5)+1, 2):
        while N % i == 0:
            N //= i
            ans += 1
    if N != 1:
        ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    ans = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            ans += 1
            n //= i
            while n%i == 0:
                n //= i
    if n != 1:
        ans += 1
    print(ans)
