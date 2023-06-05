Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print(n*2)

=======
Suggestion 2

def lcm(a, b):
    return a * b // gcd(a, b)

=======
Suggestion 3

def main():
    N = int(input())
    print(2*N)

=======
Suggestion 4

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n=int(input())
print((2*n)//gcd(2,n))

=======
Suggestion 5

def main():
    n = int(input())
    print(2*n)

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
        #print(a,b)
    return a

=======
Suggestion 7

def solve(n):
    return n * 2

n = int(input())
print(solve(n))
