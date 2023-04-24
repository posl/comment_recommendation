Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    for i in range(N):
        if i == 0:
            print(A[-2])
        elif i == N - 1:
            print(A[-2])
        else:
            if A[i] > A[i - 1]:
                print(A[-2])
            else:
                print(A[-1])

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    m = max(a)
    for i in range(n):
        if a[i] == m:
            a[i] = 0
    m = max(a)
    for i in range(n):
        if a[i] == 0:
            a[i] = m
    for i in range(n):
        print(a[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max1 = max(A)
    max2 = max([a for a in A if a != max1])
    for a in A:
        if a == max1:
            print(max2)
        else:
            print(max1)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    maxA2 = sorted(A)[-2]
    for a in A:
        if a == maxA:
            print(maxA2)
        else:
            print(maxA)

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    for i in range(n):
        if i == 0:
            print(a[n - 2])
        elif i == n - 1:
            print(a[n - 2])
        else:
            print(max(a[n - 2], a[i - 1]))

main()

You can check the submission here.

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            max_a2 = max(a[:i] + a[i + 1:])
    for i in range(n):
        if a[i] == max_a:
            print(max_a2)
        else:
            print(max_a)

main()

I got 90 points. This is my first submission.

I go

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    a = max(A)
    b = A.index(a)
    A[b] = 0
    c = max(A)
    for i in range(N):
        if i != b:
            print(c)
        else:
            print(a)

main()

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_a = max(A)
    max_a_count = A.count(max_a)
    if max_a_count > 1:
        print(*[max_a for _ in range(N)])
        return
    max_a_index = A.index(max_a)
    A[max_a_index] = 0
    max_a2 = max(A)
    print(*[max_a2 for _ in range(N)])

main()

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_ = max(A)
    max_i = A.index(max_)
    A.pop(max_i)
    max_2 = max(A)
    for i in range(N):
        if i == max_i:
            print(max_2)
        else:
            print(max_)

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]

    max_a = max(a)
    max_a_index = a.index(max_a)
    a.pop(max_a_index)
    max_a2 = max(a)

    for i in range(n):
        if i == max_a_index:
            print(max_a2)
        else:
            print(max_a)
