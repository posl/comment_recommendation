Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    if m > n:
        print("No")
        return

    for i in range(m):
        if a[i] < b[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 2

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if n < m:
        print("No")
        return
    for i in range(m):
        if b[i] < a[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    if n < m:
        print("No")
        return

    for i in range(m):
        if a[i] > b[i]:
            print("No")
            return
    print("Yes")

solve()

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < m:
        print('No')
        return

    a.sort()
    b.sort()

    for i in range(m):
        if a[i] >= b[i]:
            print('No')
            return

    print('Yes')

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()

    if n < m:
        print("No")
        return

    for i in range(m):
        if a[i] > b[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    if n < m:
        print('No')
    else:
        for i in range(n):
            if A[i] < B[i]:
                print('No')
                return
        print('Yes')

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if n < m:
        print("No")
        return
    A.sort()
    B.sort()
    for i in range(m):
        if A[i] >= B[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def solve(N,M,A,B):
    if M>N:
        return False
    A.sort()
    B.sort()
    for i in range(M):
        if B[i]<A[N-M+i]:
            return False
    return True

=======
Suggestion 9

def solve(n, m, a, b):
    if m > n:
        return False
    a.sort()
    b.sort()
    for i in range(m):
        if a[-1-i] < b[-1-i]:
            return False
    return True

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if n < m:
        print("No")
    else:
        for i in range(m):
            if a[i] >= b[i]:
                print("No")
                break
            elif i == m-1:
                print("Yes")
