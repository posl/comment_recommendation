Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    if n % 2 == 0:
        ans = n
    else:
        ans = n * 2
    print(ans)

=======
Suggestion 2

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

n = int(input())
print(n * 2 // gcd(n, 2))

=======
Suggestion 3

def lcm(a, b):
    from fractions import gcd
    return a * b // gcd(a, b)

n = int(input())
print(lcm(2, n))

=======
Suggestion 4

def main():
    n = int(input())
    for i in range(n, n * n + 1, n):
        if i % 2 == 0:
            print(i)
            break

=======
Suggestion 5

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

n = int(input())
print(n*2//gcd(n, 2))

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
print(int(n/gcd(n,2)*2))

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
print(int(n/gcd(n,2))*2)

=======
Suggestion 8

def solve(n):
    if n % 2 == 0:
        return n
    else:
        return n * 2

=======
Suggestion 9

def main():
    # input
    N = int(input())

    # compute

    # output
    print(2*N)

=======
Suggestion 10

def main():
    n = int(input())
    print(2 * n)
