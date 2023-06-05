Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def getSum(N, a, b):
    sum = 0
    for i in range(1, N + 1):
        if i % a != 0 and i % b != 0:
            sum += i
    return sum

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        c=a%b
        a=b
        b=c
    return a

=======
Suggestion 4

def f(n, a, b):
    lcm = a * b / gcd(a, b)
    return n - n / a - n / b + n / lcm

=======
Suggestion 5

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
