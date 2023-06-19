Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if m > n:
        print("No")
        return

    a.sort()
    b.sort()

    for i in range(m):
        if b[i] <= a[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if a[-1] >= b[-1]:
        print("No")
        return
    for i in range(m):
        if a[-1] >= b[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def solve(n, m, a, b):
    a.sort()
    b.sort()
    if n < m:
        return "No"
    else:
        for i in range(m):
            if a[i] >= b[i]:
                return "No"
        return "Yes"

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    if n < m:
        print("No")
    else:
        for i in range(m):
            if a[i] < b[i]:
                print("No")
                exit()
        print("Yes")

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    if N < M:
        print('No')
        return
    i = 0
    for a in A:
        if a == B[i]:
            i += 1
            if i == M:
                print('Yes')
                return
    print('No')

solve()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if m > n:
        print("No")
    else:
        a.sort()
        b.sort()
        for i in range(m):
            if a[i] > b[i]:
                print("No")
                exit()
        print("Yes")

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    if n < m:
        print('No')
        return

    for i in range(m):
        if a[i] < b[i]:
            print('No')
            return

    print('Yes')

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if m > n:
        print("No")
        return
    for i in range(m):
        if b[i] < a[i]:
            print("No")
            return
    print("Yes")
    return

main()

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            i += 1
        j += 1
    if i == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

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
