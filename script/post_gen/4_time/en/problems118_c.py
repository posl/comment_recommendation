Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        A[i+1] = A[i+1] % A[i]
    print(A[N-1])

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) > 1:
        A.sort()
        A[-1] %= A[0]
        if A[-1] == 0:
            A.pop()
    print(A[0])

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans = gcd(ans, a)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    gcd = a[0]
    for i in range(1, n):
        gcd = gcd(a[i], gcd)
    print(gcd)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    while len(A) > 1:
        A.sort()
        A[0] %= A[-1]
        if A[0] == 0:
            A.pop(0)
    print(A[0])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) > 1:
        A.sort()
        A = [a - A[0] for a in A if a > A[0]]
    print(A[0])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        print(a[0])
        exit()
    for i in range(n-2):
        a[i+1] = a[i+1] % a[0]
        if a[i+1] == 0:
            print(a[0])
            exit()
    print(a[0])

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        if A[i]*2 < A[i+1]:
            ans = i+1
    print(N-ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(gcd_list(A))
