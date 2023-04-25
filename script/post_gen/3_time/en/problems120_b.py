Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    divisors = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    print(divisors[-k])

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    div = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            div.append(i)
    print(div[-k])

=======
Suggestion 3

def main():
    a, b, k = map(int, input().split())
    div = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            div.append(i)
    print(div[-k])

=======
Suggestion 4

def main():
    a, b, k = map(int, input().split())
    div = [i for i in range(1, min(a, b)+1) if a % i == 0 and b % i == 0]
    print(div[-k])

=======
Suggestion 5

def getDivisor(a, b):
    divisor = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisor.append(i)
    return divisor

=======
Suggestion 6

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

a, b, k = map(int, input().split())
c = gcd(a, b)
d = []
for i in range(1, c+1):
    if c%i == 0:
        d.append(i)
print(d[-k])

=======
Suggestion 7

def main():
    a, b, k = map(int, input().split())
    counter = 0
    for i in range(1, max(a, b)+1):
        if a % i == 0 and b % i == 0:
            counter += 1
            if counter == k:
                print(i)
                break

=======
Suggestion 8

def main():
    A, B, K = [int(x) for x in input().split()]
    d = []
    for i in range(1, max(A, B)+1):
        if A % i == 0 and B % i == 0:
            d.append(i)
    print(d[-K])

=======
Suggestion 9

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
