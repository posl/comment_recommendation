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
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        a[i+1] = a[i+1] % a[i]
    print(a[-1])

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans = ans ^ a[i]
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i+1] % A[i] == 0:
            A[i+1] = A[i]
    print(A[N-1])

=======
Suggestion 6

def solve(N, A):
    while len(A) > 1:
        A.sort()
        A[-1] = A[-1] % A[0]
        if A[-1] == 0:
            A.pop(-1)
    return A[0]

N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1,n):
        a[i] = a[i] % a[0]
    if a[0] == 1:
        print(1)
        return
    if a[0] == 0:
        print(0)
        return
    a[0] = a[0] % a[1]
    if a[1] == 1:
        print(1)
        return
    if a[1] == 0:
        print(0)
        return
    print(a[1])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(gcd_list(a))

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    import math
    print(math.gcd(a[0], a[-1]))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    for i in range(n-1):
        if a[i] > 1:
            a[i+1] = a[i+1] % a[i]
            if a[i+1] == 0:
                a[i+1] = a[i]
    print(a[-1])
