Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 3

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 4

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b,c,d=map(int,input().split())
g=gcd(c,d)
lcm=c*d//g
print(b-a+1-(b//c-(a-1)//c)-(b//d-(a-1)//d)+(b//lcm-(a-1)//lcm))

=======
Suggestion 5

def getNum(A,B,C,D):
    res = 0
    for i in range(A,B+1):
        if i % C == 0 and i % D == 0:
            res += 1
    return res
