Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    for i in range(N):
        print(max(A[:i] + A[i+1:]))

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        print(max(a[:i] + a[i+1:]))

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    a_max_index = a.index(a_max)
    for i in range(n):
        if i == a_max_index:
            print(max(a[:i] + a[i+1:]))
        else:
            print(a_max)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    a_max2 = sorted(a)[-2]
    for i in range(n):
        if a[i] == a_max:
            print(a_max2)
        else:
            print(a_max)

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    second_max_a = sorted(a)[-2]
    for i in range(n):
        if a[i] == max_a:
            print(second_max_a)
        else:
            print(max_a)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max = max(A)
    for i in range(N):
        if A[i] == max:
            A[i] = 0
            print(max(A))
            A[i] = max

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    a_max = max(a)
    a_max2 = max(a[:a.index(a_max)] + a[a.index(a_max)+1:])
    for i in range(n):
        if a[i] == a_max:
            print(a_max2)
        else:
            print(a_max)

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        a_sort = sorted(a)
        if a[i] == a_sort[-1]:
            print(a_sort[-2])
        else:
            print(a_sort[-1])

=======
Suggestion 9

def main():
    n = int(input())
    a_list = []
    for i in range(n):
        a_list.append(int(input()))
    max_a = max(a_list)
    max_a2 = sorted(a_list)[-2]
    for i in range(n):
        if a_list[i] != max_a:
            print(max_a)
        else:
            print(max_a2)

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))

    max_A = max(A)
    max_A_index = A.index(max_A)
    A.pop(max_A_index)

    for i in range(N):
        if i == max_A_index:
            print(max(A))
        else:
            print(max_A)
