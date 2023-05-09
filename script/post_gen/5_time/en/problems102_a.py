Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n=int(input())
print(2*n//gcd(2,n))

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())

print(int(2*N/gcd(2, N)))

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N=int(input())
print(2*N//gcd(2,N))

=======
Suggestion 6

def main():
    n = int(input())
    print(2*n)

=======
Suggestion 7

def main():
    n = int(input())
    print(n*2)

=======
Suggestion 8

def main():
    N = int(input())
    print(int(N*(N%2+1)/2))

=======
Suggestion 9

def main():
    n = int(input())
    print(2*n)
    return
