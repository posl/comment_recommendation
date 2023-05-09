Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        if (i % a != 0) and (i % b != 0):
            sum += i
    print(sum)

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def getSum(n, a, b):
    sum = 0
    for i in range(1, n+1):
        if i % a != 0 and i % b != 0:
            sum += i
    return sum

=======
Suggestion 6

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    print(sum([i for i in range(1,N+1) if i%A != 0 and i%B != 0]))
