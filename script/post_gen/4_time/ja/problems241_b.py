Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if M > N:
        print("No")
        return

    A.sort()
    B.sort()

    for i in range(M):
        if B[i] < A[i]:
            print("No")
            return

    print("Yes")

main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        print("No")
        return

    A.sort()
    B.sort()

    for i in range(M):
        if A[i] > B[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if M > N:
        print('No')
        return

    A.sort()
    B.sort()

    for i in range(M):
        if A[N - i - 1] < B[M - i - 1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if m > n:
        print("No")
        return

    a.sort()
    b.sort()

    for i in range(m):
        if a[n - i - 1] < b[m - i - 1]:
            print("No")
            return

    print("Yes")

main()

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < m:
        print("No")
        return

    for i in range(m):
        if b[i] not in a:
            print("No")
            return

    print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if min(A) < min(B):
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            i += 1
        j += 1
    if i == n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if M > N:
        print("No")
    else:
        A.sort()
        B.sort()
        for i in range(M):
            if A[N-i-1] < B[M-i-1]:
                print("No")
                exit()
        print("Yes")

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    cnt = 0
    for i in range(M):
        for j in range(cnt,N):
            if A[j] >= B[i]:
                cnt += 1
                break
    if cnt >= M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N<M:
        print("No")
        exit()
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(M):
        if A[i]<B[i]:
            print("No")
            exit()
    print("Yes")
