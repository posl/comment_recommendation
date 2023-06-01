Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem161_b():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] < (total/(4*m)):
            print('否')
            return
    print('是')

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum += a[i]
    if a[m-1] >= sum/(4*m):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] < total/(4*m):
            print("否")
            return
    print("是")

=======
Suggestion 4

def readinput():
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,m,a

=======
Suggestion 5

def problems161_b():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum_a = sum(a)
    if a[m-1] >= sum_a / (4*m):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def problems161_b():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    s = sum(a)
    if a[m-1] >= s/(4*m):
        print("是")
    else:
        print("否")

=======
Suggestion 7

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort(reverse=True)
    total=sum(A)
    if A[M-1]*4*M>=total:
        print("是")
    else:
        print("否")

=======
Suggestion 8

def get_input():
    n,m = input().split()
    n = int(n)
    m = int(m)
    A = input().split()
    A = [int(i) for i in A]
    return n,m,A

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1]*4*m >= total:
        print("是")
    else:
        print("否")
