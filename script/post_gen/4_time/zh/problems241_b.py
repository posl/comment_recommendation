Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()
    B.sort()

    if N < M:
        print("No")
        return

    if min(A) < min(B):
        print("No")
        return

    for i in range(M):
        if A[i] > B[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 2

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #a = sorted(a)
    #b = sorted(b)

    if m > n:
        print("No")
    else:
        #for i in range(m):
        #    if b[i] > a[i]:
        #        print("No")
        #        exit()
        #print("Yes")
        a.sort()
        b.sort()
        for i in range(m):
            if b[i] < a[i]:
                print("No")
                exit()
        print("Yes")

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if n<m:
        print('No')
        return
    for i in range(m):
        if a[i]>=b[i]:
            print('No')
            return
    print('Yes')
main()

=======
Suggestion 4

def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if m > n:
        return 'No'

    a.sort()
    b.sort()

    for i in range(m):
        if a[n-m+i] < b[i]:
            return 'No'
    return 'Yes'

=======
Suggestion 5

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
        if a[n - i - 1] < b[m - i - 1]:
            print('No')
            return

    print('Yes')

=======
Suggestion 6

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if n < m:
        print("No")
    else:
        a.sort()
        b.sort()
        for i in range(m):
            if a[i] < b[i]:
                print("No")
                return
        print("Yes")
solve()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N < M:
        print('No')
    else:
        A.sort()
        B.sort()
        for i in range(N - M + 1):
            if A[i:i + M] == B:
                print('Yes')
                break
        else:
            print('No')

=======
Suggestion 8

def solution():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if n < m:
        print('No')
        return
    for i in range(m):
        if a[i] >= b[i]:
            print('No')
            return
    print('Yes')

solution()

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(m):
        if a[i] < b[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if m > n:
        print('No')
        return

    a.sort()
    b.sort()

    for i in range(m):
        if a[n - 1 - i] < b[m - 1 - i]:
            print('No')
            return

    print('Yes')
