Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(M):
        if A[i] < sum / (4 * M):
            print('No')
            return
    print('Yes')
main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total/(4*M):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = 0
    for a in A:
        total += a
    for i in range(M):
        if A[i] < total / (4 * M):
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print('Yes' if a[m-1] >= sum(a) / (4*m) else 'No')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse = True)
    if A[M-1] >= sum(A) / (4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    print("Yes" if a[m-1] >= total / (4*m) else "No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total / (4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    if A[M-1] >= sum(A) / (4*M):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    total = sum(A)
    threshold = total // (4 * M)

    if A[M-1] >= threshold:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n, m, *a = map(int, open(0).read().split())
    a.sort(reverse = True)
    print("Yes" if a[m - 1] >= sum(a) / (4 * m) else "No")
main()
