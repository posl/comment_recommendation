Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    div = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            div.append(i)
    print(div[-k])

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
    print(divisors[-k])

=======
Suggestion 3

def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 4

def get_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 5

def main():
    A, B, K = map(int, input().split())
    divisors = []
    for i in range(1, min(A,B)+1):
        if A % i == 0 and B % i == 0:
            divisors.append(i)
    print(divisors[-K])

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

a, b, k = map(int, input().split())
c = gcd(a,b)
cnt = 0
for i in range(c,0,-1):
    if c%i==0:
        cnt += 1
    if cnt==k:
        print(i)
        break

=======
Suggestion 7

def divisors(n):
    l = []
    for i in range(1, n+1):
        if n%i == 0:
            l.append(i)
    return l

a, b, k = map(int, input().split())
div = divisors(a) + divisors(b)
div = list(set(div))
div.sort(reverse=True)
print(div[k-1])

=======
Suggestion 8

def main():
    # input
    A, B, K = map(int, input().split())
    # compute
    divisors = []
    for i in range(1, min(A, B)+1):
        if A%i==0 and B%i==0:
            divisors.append(i)
    # output
    print(divisors[-K])

=======
Suggestion 9

def get_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors
