Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        for j in range(i+1, N):
            if (A[i]+A[j])%2 == 0:
                print(A[i]+A[j])
                return
    print(-1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        for i in range(n-1, 0, -1):
            if a[i] % 2 == 0:
                print(a[i])
                break
            elif (a[i] + a[i-1]) % 2 == 0:
                print(a[i] + a[i-1])
                break
            elif i == 1:
                print(-1)

=======
Suggestion 3

def solve(n, a):
    a.sort()
    max_even = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                max_even = max(max_even, a[i] + a[j])
                break
    return max_even

=======
Suggestion 4

def solve(N, A):
    A.sort()
    if A[-1] < 2:
        return -1
    if A[-1] == 2:
        return 2
    for i in range(N-1):
        if A[i] == A[i+1]:
            return A[i]*2
    return -1

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        if a[0] % 2 == 0:
            print(a[0] + a[1])
        else:
            print(-1)
    else:
        if a[0] % 2 == 0:
            print(a[0] + a[1])
        else:
            print(a[-1] + a[-2])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a = sorted(a)
    if a[0] == 0:
        print(-1)
    else:
        if a[0] % 2 == 0:
            print(a[0])
        else:
            print(-1)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] % 2 == 0:
        print(a[0])
    elif a[1] % 2 == 0:
        print(a[1])
    elif a[0] + a[1] % 2 == 0:
        print(a[0] + a[1])
    else:
        print(-1)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_even = -1
    for i in range(N-1):
        if A[i] == A[i+1]:
            max_even = A[i]*2
    print(max_even)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    max_even = -1
    for i in range(N-1):
        if A[i] == A[i+1]:
            max_even = A[i]
    print(max_even)

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
        return
    for i in range(N-1, 0, -1):
        for j in range(i-1, -1, -1):
            if (A[i] + A[j]) % 2 == 0:
                print(A[i] + A[j])
                return
    print(-1)
    return
