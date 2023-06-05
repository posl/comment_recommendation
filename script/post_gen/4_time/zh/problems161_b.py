Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum_a = sum(a)
    sum_b = 0
    for i in range(m):
        if a[i] < sum_a / (4 * m):
            print("No")
            return
        sum_b += a[i]
    if sum_b >= sum_a / 4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] < total/(4*m):
            print("否")
            exit()
    print("是")

=======
Suggestion 3

def problems161_b():
    n,m = input().split()
    n = int(n)
    m = int(m)
    A = input().split()
    A = list(map(int,A))
    A.sort(reverse=True)
    total = sum(A)
    for i in range(m):
        if A[i] < total/(4*m):
            print("否")
            return
    print("是")
    return

=======
Suggestion 4

def problems161_b():
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
Suggestion 5

def problems161_b():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    if a[m-1] >= sum(a)/(4*m):
        print("是")
    else:
        print("否")

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    s = sum(A)
    for i in range(m):
        if A[i] < s / (4 * m):
            print('否')
            exit()
    print('是')

=======
Suggestion 7

def problems161_b():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(N):
        sum += A[i]
    if A[M-1] >= sum /(4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = sum(a)
    a.sort(reverse=True)
    if a[m-1] >= sum_a / (4*m):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total/(4*m):
        print("是")
    else:
        print("否")

=======
Suggestion 10

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum += a[i]
    if a[m-1] >= sum/(4*m):
        print("Yes")
    else:
        print("No")
