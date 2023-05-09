Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[M-1] >= sum(A)/(4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    if a[m-1] >= sum(a) / (4*m):
        print('Yes')
    else:
        print('No')

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
            return
    print("Yes")

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = sum(a)
    for i in range(m):
        if a[i] * 4 * m < s:
            print("No")
            return
    print("Yes")

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

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total/(4*m):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    a.sort(reverse=True)
    if a[m-1] * 4 * m >= total:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total / (4 * m):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    total = sum(a)
    for i in range(m):
        if a[i] < total * 1/(4*m):
            print("No")
            return
    print("Yes")
