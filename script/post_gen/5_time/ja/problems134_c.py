Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
    a_max = max(a)
    a_max_index = a.index(a_max)
    for i in range(n):
        if i == a_max_index:
            print(max(a[:i] + a[i + 1:]))
        else:
            print(a_max)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    for i in range(n):
        print(max(a[:i] + a[i+1:]))

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    B = sorted(A)
    for i in range(N):
        if A[i] == B[-1]:
            print(B[-2])
        else:
            print(B[-1])

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]

    max_a = max(a)
    max_a_index = a.index(max_a)

    for i in range(n):
        if i == max_a_index:
            print(max(a[:i] + a[i+1:]))
        else:
            print(max_a)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    for i in range(N):
        if A[i] == max(A):
            print(max(A[:i]+A[i+1:]))
        else:
            print(max(A))

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    a_max = a[-1]
    for i in range(n):
        if a_max == a[i]:
            print(a[-2])
        else:
            print(a_max)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_index = a.index(a_max)
    for i in range(n):
        if i == a_max_index:
            print(sorted(a[:a_max_index]+a[a_max_index+1:])[-1])
        else:
            print(a_max)

=======
Suggestion 8

def main():
    n = int(input())
    a_list = []
    for _ in range(n):
        a = int(input())
        a_list.append(a)

    for i in range(n):
        b_list = a_list.copy()
        b_list.pop(i)
        print(max(b_list))

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    for i in range(N):
        print(max(A[:i]+A[i+1:]))

=======
Suggestion 10

def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())

    max1 = max(a)
    a.remove(max1)
    max2 = max(a)
    a.append(max1)

    for i in range(n):
        if a[i] == max1:
            print(max2)
        else:
            print(max1)
