Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total/(4*M):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    if A[M-1] >= sum(A)/(4*M):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] < total/(4*m):
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1]*4*m >= total:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b = sum(a) / (4 * m)
    for i in range(m):
        if a[i] < b:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for a in A:
        sum += a
    if A[M-1] >= sum / (4 * M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] < total / (4*M):
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    ans = "No"
    if a[m-1] >= total/(4*m):
        ans = "Yes"
    print(ans)

=======
Suggestion 9

def check():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum >= sum(a) / (4*m):
        print("Yes")
    else:
        print("No")

check()

=======
Suggestion 10

def check(a):
    if a >= sum(A) * (1 / (4 * M)):
        return True
    else:
        return False

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
