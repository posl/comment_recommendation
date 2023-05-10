Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = sum(a)
    for i in range(m):
        if a[i] < s / (4 * m):
            print('No')
            exit()
    print('Yes')

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    for i in range(M):
        if A[i] < sum/(4*M):
            print("No")
            exit()
    print("Yes")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] < total / (4 * m):
            print("No")
            exit()
    print("Yes")
main()

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if a[m-1] >= sum(a)/(4*m):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum >= sum(a) / (4 * m):
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
    for i in range(m):
        if a[i] < total / (4 * m):
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total/(4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    SUM = sum(A)
    for i in range(M):
        if A[i] < SUM / (4*M):
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 9

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(m):
        if a[i] < sum * (1/(4*m)):
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    total = sum(A)
    limit = total / (4 * M)

    if A[M-1] >= limit:
        print("Yes")
    else:
        print("No")
