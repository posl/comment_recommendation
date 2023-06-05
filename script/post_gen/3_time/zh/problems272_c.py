Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    ans = -1
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                ans = max(ans, A[i] + A[j])
    print(ans)

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    max_even = -1
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                max_even = max(max_even, A[i]+A[j])
    print(max_even)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 0:
        print(-1)
    elif N == 2:
        if A[0] % 2 == 0:
            print(A[0])
        else:
            print(-1)
    else:
        if A[0] % 2 == 0:
            print(A[0])
        else:
            print(A[0] + A[1])
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 1:
        print(-1)
    else:
        for i in range(n-1):
            if a[i] == a[i+1]:
                print(a[-1])
                break
        else:
            print(-1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_even = -1
    for i in range(N):
        if A[i] % 2 == 0:
            max_even = A[i]
    if max_even == -1:
        print(-1)
    else:
        for i in range(N):
            for j in range(i+1, N):
                if A[i] + A[j] == max_even:
                    print(max_even)
                    return
        print(-1)
        return

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    if a[0] % 2 == 1:
        print(-1)
    else:
        for i in range(1, n):
            if a[i] % 2 == 0:
                print(a[0])
                break
        else:
            print(-1)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] == 0:
        a.pop(0)
    for i in range(len(a)-1, 0, -1):
        if a[i] == a[i-1]:
            a.pop(i)
    a.sort()
    #print(a)
    for i in range(len(a)-1, 0, -1):
        if a[i] % 2 == 0:
            print(a[i])
            return
        else:
            for j in range(i-1, -1, -1):
                if (a[i] + a[j]) % 2 == 0:
                    print(a[i]+a[j])
                    return
    print(-1)
    return

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] + A[j] > max and (A[i] + A[j])%2 == 0:
                max = A[i] + A[j]
    if max == 0:
        print(-1)
    else:
        print(max)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_even = -1
    for i in range(N):
        if A[i] % 2 == 0:
            max_even = A[i]
        else:
            for j in range(i + 1, N):
                if (A[i] + A[j]) % 2 == 0:
                    max_even = max(max_even, A[i] + A[j])
                    break
    print(max_even)
