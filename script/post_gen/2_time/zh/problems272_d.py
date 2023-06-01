Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[0] == 0:
        print(-1)
        exit()
    if n == 1:
        print(-1)
        exit()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print(a[i] * 2)
            exit()
    print(-1)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 0:
        print(-1)
    else:
        print(A[-1] + A[-2])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_even = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i]+a[j])%2 == 0:
                if max_even < a[i]+a[j]:
                    max_even = a[i]+a[j]
    print(max_even)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j])%2 == 0:
                print(a[i]+a[j])
                return
    print(-1)
    return

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[N-1] % 2 == 0:
        print(A[N-1])
        return
    else:
        for i in range(N-1):
            if A[i] % 2 == 0:
                print(A[N-1] + A[i])
                return
    print(-1)
    return

main()

=======
Suggestion 6

def evenSum(n, a):
    a.sort()
    if a[0] == 0 and a[1] == 0:
        return 0
    elif a[0] == 0 and a[1] == 1:
        return -1
    elif a[0] == 0 and a[1] > 1:
        return a[1] - 1
    elif a[0] == 1:
        return -1
    else:
        return a[0] + a[1]

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        for i in range(n-1, -1, -1):
            for j in range(i-1, -1, -1):
                if (a[i] + a[j]) % 2 == 0:
                    print(a[i] + a[j])
                    break
                if j == 0:
                    print(-1)
                    break
            if a[i] % 2 == 0:
                break

=======
Suggestion 8

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
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]+a[j])%2 == 0:
                print(a[i]+a[j])
                return
    print(-1)
main()

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
        return
    for i in range(N-1):
        if A[i] % 2 == 0:
            print(A[i])
            return
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                print(A[i]+A[j])
                return
    print(-1)
    return
