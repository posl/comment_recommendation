Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 2

def problem131_c():
    a,b,c,d = map(int,input().split())
    cnt = 0
    for i in range(a,b+1):
        if i % c == 0 and i % d == 0:
            cnt += 1
    print(cnt)

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
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 5

def gcd(a,b):
    if a<b:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

=======
Suggestion 7

def get_num(x, y, a, b):
    return b//x - (a-1)//x + b//y - (a-1)//y - b//(x*y) + (a-1)//(x*y)

a, b, c, d = map(int, input().split())
print(get_num(c, d, a, b))
