Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        n -= a[i]
        if n < 0:
            print(m - i)
            return
    print(-1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(-1)
            return
    print(N)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        if A[i] <= N:
            N -= A[i]
        else:
            print(N)
            return
    print(-1)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        n -= a[i]
    if n < 0:
        print(-1)
    else:
        print(n)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    sum_A = sum(A)
    if sum_A > N:
        print(-1)
    else:
        print(N - sum_A)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        if N - A[i] < 0:
            print(N)
            exit()
        else:
            N -= A[i]
    print(-1)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list.sort()
    for a in a_list:
        n -= a
        if n < 0:
            print(-1)
            return
    print(n)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    for i in range(M):
        N = N - A[i]
        if N < 0:
            print(-1)
            return

    print(N)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        N -= A[i]
    print(N)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    A.sort()
    #print(A)
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(-1)
            return
    print(N)
