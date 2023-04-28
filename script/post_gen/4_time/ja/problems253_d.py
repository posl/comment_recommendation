Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    sum = 0
    for i in range(1, n + 1):
        if i % a == 0 or i % b == 0:
            continue
        sum += i
    print(sum)

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        if (i % a != 0) and (i % b != 0):
            ans += i
    print(ans)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a

    return gcd(b, a % b)

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    ans = 0
    ans += n // a
    ans += n // b
    ans -= n // (a*b)
    print(n*(n+1)//2 - ans*(ans+1)//2)

=======
Suggestion 7

def main():
    n,a,b = map(int, input().split())
    ans = 0
    ans += n // a
    ans += n // b
    ans -= n // (a*b//gcd(a,b))
    print(ans)

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n,a,b = map(int,input().split())
g = gcd(a,b)
lcm = a*b//g
n1 = n//a
n2 = n//b
n3 = n//lcm
print(n*(n+1)//2 - (n1+n2-n3)*(a+b)//2)

=======
Suggestion 9

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

N,A,B = map(int,input().split())

lcm = A*B//gcd(A,B)

print((N//A+N//B-N//lcm)*A+(N//B-N//lcm)*B)

=======
Suggestion 10

def main():
    N, A, B = map(int, input().split())
    print(sum([x for x in range(1, N+1) if x % A and x % B]))
