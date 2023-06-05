Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    count = 0
    for i in range(A, B+1):
        if i % C == 0 and i % D == 0:
            count += 1
    print(count)

=======
Suggestion 2

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 4

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

a,b,c,d = map(int, input().split())

cd = c*d//gcd(c,d)

print(b-a+1-(b//c-(a-1)//c+b//d-(a-1)//d-b//cd+(a-1)//cd))

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

A, B, C, D = map(int, input().split())
g = gcd(C, D)
lcm = C * D // g

=======
Suggestion 6

def main():
    A,B,C,D = map(int, input().split())
    a = A // C
    b = B // C
    c = A // D
    d = B // D
    e = A // (C * D)
    f = B // (C * D)
    if A % C == 0:
        a -= 1
    if A % D == 0:
        c -= 1
    if A % (C * D) == 0:
        e -= 1
    print(B - A + 1 - (b - a) - (d - c) + (f - e))

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a,b,c,d = map(int,input().split())
#求最小公倍数
lcm = c*d//gcd(c,d)
#求出最小公倍数在[a,b]区间内的个数
ans = b//lcm - (a-1)//lcm
print(ans)

=======
Suggestion 8

def gcd(m, n):
    if m < n:
        m, n = n, m
    while n != 0:
        m, n = n, m % n
    return m
