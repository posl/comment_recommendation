Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
print(n * 2 // gcd(n, 2))

=======
Suggestion 2

def main():
    n = int(input())
    if n % 2 == 0:
        print(n)
    else:
        print(n * 2)

=======
Suggestion 3

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

n=int(input())
print(n*2//gcd(n,2))

=======
Suggestion 4

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

N = int(input())
ans = 2*N//gcd(2,N)
print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    print(2*N)

=======
Suggestion 6

def main():
    n = int(input())
    print(2 * n)

=======
Suggestion 7

def main():
    n = int(input())
    print(n*2)
