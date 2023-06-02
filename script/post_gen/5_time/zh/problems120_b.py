Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

A, B, K = map(int, input().split())
gcd = gcd(A, B)
ans = []
for i in range(1, gcd + 1):
    if gcd % i == 0:
        ans.append(i)
print(ans[-K])

=======
Suggestion 2

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

=======
Suggestion 3

def get_gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 4

def main():
    a,b,k = map(int,input().split())
    if a > b:
        a,b = b,a
    count = 0
    for i in range(b,0,-1):
        if a%i == 0 and b%i == 0:
            count += 1
            if count == k:
                print(i)
                break

=======
Suggestion 5

def problem120_b():
    A, B, K = map(int, input().split())
    divisors = []
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            divisors.append(i)
    print(divisors[-K])

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

=======
Suggestion 7

def main():
    a,b,k = map(int,input().split())
    alist = []
    blist = []

    for i in range(1,101):
        if a % i == 0:
            alist.append(i)
        if b % i == 0:
            blist.append(i)
    alist.reverse()
    blist.reverse()
    #print(alist)
    #print(blist)
    clist = []
    for i in alist:
        for j in blist:
            if i == j:
                clist.append(i)
    #print(clist)
    print(clist[k-1])

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b, k = map(int, input().split())
c = gcd(a, b)
l = []
for i in range(1, c + 1):
    if c % i == 0:
        l.append(i)
print(l[-k])

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b, k = map(int, input().split())
c = gcd(a, b)

cnt = 0
for i in range(c, 0, -1):
    if c % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break

=======
Suggestion 10

def func(a,b,k):
    count = 0
    for i in range(1,101):
        if a%i==0 and b%i==0:
            count += 1
            if count == k:
                return i
