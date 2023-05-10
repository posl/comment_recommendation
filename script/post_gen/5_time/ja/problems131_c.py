Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 4

def main():
    a,b,c,d = map(int, input().split())
    e = c*d
    f = b//c - (a-1)//c
    g = b//d - (a-1)//d
    h = b//e - (a-1)//e
    print(b-a+1-f-g+h)

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    ans = b - a + 1
    ans -= b // c - (a-1) // c
    ans -= b // d - (a-1) // d
    ans += b // (c * d) - (a-1) // (c * d)
    print(ans)

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 7

def main():
    # input
    A, B, C, D = map(int, input().split())

    # compute
    cnt = 0
    for i in range(A, B+1):
        if i % C != 0 and i % D != 0:
            cnt += 1

    # output
    print(cnt)

=======
Suggestion 8

def main():
    a,b,c,d = map(int,input().split())
    def gcd(x,y):
        if y == 0:
            return x
        else:
            return gcd(y,x%y)
    def lcm(x,y):
        return x*y//gcd(x,y)
    def f(x):
        return x-(x//c+x//d-x//lcm(c,d))
    print(f(b)-f(a-1))
