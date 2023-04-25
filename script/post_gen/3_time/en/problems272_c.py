Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
    else:
        for i in range(N-1):
            if A[i] % 2 == 0:
                print(A[i])
                return
        print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    if A[-1] % 2 == 0:
        print(A[-1])
    else:
        for i in range(N-1):
            if A[i] % 2 == 0:
                print(A[i])
                break
        else:
            print(-1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 1:
        print(-1)
    else:
        print(A[-1] + A[-2])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
    else:
        for i in range(N-1):
            if A[i] % 2 == 1:
                print(A[i])
                break
        else:
            print(-1)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    elif a[-1] % 2 == 1:
        for i in range(n-1):
            if a[i] % 2 == 1:
                print(a[i] + a[i+1])
                break
        else:
            print(-1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(0, N):
        for j in range(i + 1, N):
            if A[i] % 2 == 0:
                if A[i] == A[j] * 2:
                    print(A[i])
                    return
            else:
                if A[i] == A[j] * 2 + 1:
                    print(A[i])
                    return
    print(-1)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        if a[-2] % 2 == 0:
            print(a[-2])
        else:
            print(-1)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 1000000001
    for i in range(N):
        B[A[i]] = 1
    for i in range(N):
        for j in range(i+1, N):
            if B[A[i] + A[j]] == 1:
                B[A[i] + A[j]] = 2
    for i in range(1000000000, -1, -2):
        if B[i] == 2:
            print(i)
            return
    print(-1)

=======
Suggestion 9

def solve(N, A):
    A.sort()
    if A[-1] % 2 == 1:
        return -1
    else:
        return A[-1]

=======
Suggestion 10

def solve(A,N):
    A.sort()
    if A[-1] % 2 == 1:
        return -1
    else:
        return A[-1]
