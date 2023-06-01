Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
n,m = map(int, input().split())

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
c = gcd(n, m)
print(m // c)

=======
Suggestion 3

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

n,m = map(int,input().split())
a = gcd(n,m)
print(int(m/a))

=======
Suggestion 4

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, M = map(int, input().split())

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 7

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 8

def gcd(a,b):
	while b:
		a,b = b,a%b
	return a

n,m = map(int,input().split())

=======
Suggestion 9

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
a = gcd(n, m)
print(m // a)
