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

def f(n,a,b):
    count = 0
    for i in range(1,n+1):
        if i%a != 0 and i%b != 0:
            count += i
    return count

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    print(sum([i for i in range(1, n+1) if (i%a)*(i%b)!=0]))

=======
Suggestion 4

def getSum(n, a, b):
    sum = 0
    for i in range(1, n+1):
        if i % a != 0 and i % b != 0:
            sum += i
    return sum

=======
Suggestion 5

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

=======
Suggestion 6

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    print(sum([i for i in range(1, n+1) if i % a and i % b]))

=======
Suggestion 8

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    sum = 0
    for i in range(N + 1):
        if i % A != 0 and i % B != 0:
            sum += i
    print(sum)
