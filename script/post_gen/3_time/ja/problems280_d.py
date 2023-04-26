Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    n = 0
    for i in range(2, k+1):
        if k % i == 0:
            n = i
            break
    print(n)

=======
Suggestion 2

def main():
    k = int(input())
    n = 1
    while True:
        if n % 2 == 0 or n % 5 == 0:
            n += 1
            continue
        if k % n == 0:
            print(n)
            break
        n += 1

=======
Suggestion 3

def main():
    K = int(input())
    N = 1
    while True:
        if N % K == 0:
            print(N)
            break
        N += 1

=======
Suggestion 4

def main():
    K = int(input())
    n = 2
    while True:
        if K % n == 0:
            print(n)
            break
        else:
            n += 1

=======
Suggestion 5

def main():
    k = int(input())
    n = 1
    for i in range(2, k):
        n *= i
        if n%k==0:
            print(i)
            break

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 7

def main():
    k = int(input())
    n = k
    while True:
        if n % k == 0:
            break
        n += k
    print(n)

=======
Suggestion 8

def main():
    k = int(input())
    n = 1
    while True:
        #print(n)
        if k%n == 0:
            n += 1
        else:
            print(n)
            break
