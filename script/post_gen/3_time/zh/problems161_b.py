Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    if a[m-1]*4*m>=sum(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(M):

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total/(4*m):
        print("Yes")
    else

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum_a = sum(a)
    if a[m-1] >= sum_a/(4*m):
        print("Yes")
    else

=======
Suggestion 5

def problems161_b():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += A[i]
    if sum >=

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum_a = sum(a)
    for i in range(m):
        if a[i] < sum_a / (4 * m)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum += a[i]
    if a[m-1] >= su

=======
Suggestion 8

def main():
    n,m=input().split()
    n=int(n)
    m=int(m)
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    sum=0
    for i in range(m):
        sum+=a[i]
    for i in r

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(N):
        sum += A[i]
    if A[M-1] >= sum

=======
Suggestion 10

def problems161_b():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in r
