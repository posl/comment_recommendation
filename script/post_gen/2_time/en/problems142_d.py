Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 4

def divisor(n):
    i = 1
    result = []
    while i*i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n//i)
        i += 1
    result.sort()
    return result

=======
Suggestion 5

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 6

def gcd(a,b):
    if a<b:
        a,b = b,a
    if b==0:
        return a
    return gcd(b,a%b)
