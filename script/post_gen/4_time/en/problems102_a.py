Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
print(int(2*n/gcd(2, n)))

=======
Suggestion 2

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
print(n * 2 // gcd(n, 2))

=======
Suggestion 3

def main():
    n = int(input())
    if n % 2 == 0:
        print(n)
    else:
        print(n*2)

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
print(int(n / gcd(n, 2) * 2))

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
print(n*2//gcd(n,2))

=======
Suggestion 6

def main():
    N = int(input())
    print(2*N)

=======
Suggestion 7

def main():
    N = int(input())
    print(2*N if N%2==0 else 2*N)
main()

=======
Suggestion 8

def main():
    n = int(input())
    print(2 * n)

=======
Suggestion 9

def get_min_divisible_by_2_and_n(n):
    return 2 * n
