Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] < (total/(4*m)):
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[M-1] >= sum(A)/(4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m - 1] * 4 * m >= total:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    A.sort(reverse=True)
    if A[M-1] >= total/(4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total/(4*M):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total/(4*m):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    A.sort(reverse=True)
    if A[M-1] >= total / (4*M):
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= (total / (4 * M)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    
    total = sum(A)
    A.sort(reverse=True)
    
    if A[M-1] >= (total/(4*M)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def solve(n, m, a):
