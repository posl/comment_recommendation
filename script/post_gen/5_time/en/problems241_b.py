Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] == B[j]:
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            print("No")
            exit()
    if j == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < m:
        print("No")
        return

    a.sort()
    b.sort()

    for i in range(m):
        if a[i] > b[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < m:
        print('No')
    else:
        a.sort()
        b.sort()
        for i in range(m):
            if a[n - m + i] < b[i]:
                print('No')
                break
        else:
            print('Yes')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if M > N:
        print("No")
    else:
        A.sort()
        B.sort()
        i = 0
        j = 0
        while i < M and j < N:
            if B[i] <= A[j]:
                i += 1
            j += 1
        if i == M:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N < M:
        print("No")
        return
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(M):
        if A[i] < B[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if M > N:
        print('No')
    else:
        A.sort()
        B.sort()
        for i in range(M):
            if A[i] > B[i]:
                print('No')
                exit()
        print('Yes')

=======
Suggestion 7

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] <= B[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if m > n:
        print("No")
    elif m == n:
        if a == b:
            print("Yes")
        else:
            print("No")
    elif m < n:
        a.sort()
        b.sort()
        c = []
        for i in range(n):
            if a[i] in b:
                c.append(a[i])
        if c == b:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def input_to_int():
    return list(map(int,input().split()))

n,m = input_to_int()
a = input_to_int()
b = input_to_int()

a.sort()
b.sort()

j = 0
for i in range(n):
    if j == m:
        break
    if a[i] <= b[j]:
        j += 1

=======
Suggestion 10

def input():
    return raw_input()
