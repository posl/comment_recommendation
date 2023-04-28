Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            print(sorted(a)[n-2])
        else:
            print(max_a)

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        print(max(a[:i]+a[i+1:]))

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_a = max(a)
    max_a_index = a.index(max_a)
    for i in range(n):
        if i == max_a_index:
            print(max(a[:max_a_index] + a[max_a_index+1:]))
        else:
            print(max_a)

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_a_index = a.index(max_a)
    for i in range(n):
        if i == max_a_index:
            print(max(a[0:i]+a[i+1:n]))
        else:
            print(max_a)

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    max_a = max(a)
    max_a_index = a.index(max_a)

    for i in range(n):
        if i == max_a_index:
            print(max(a[:i]+a[i+1:]))
        else:
            print(max_a)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    for i in range(N):
        if A[i] == maxA:
            print(max(A[:i] + A[i+1:]))
        else:
            print(maxA)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_value = max(a)
    for i in range(n):
        if a[i] == max_value:
            print(max(a[:i]+a[i+1:]))
        else:
            print(max_value)

=======
Suggestion 8

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    max_a = max(a_list)
    max_a_index = a_list.index(max_a)
    for i in range(n):
        if i == max_a_index:
            print(max(a_list[:max_a_index] + a_list[max_a_index+1:]))
        else:
            print(max_a)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_max = max(A)
    A_max_idx = A.index(A_max)
    for i in range(N):
        if i == A_max_idx:
            print(max(A[:i]+A[i+1:]))
        else:
            print(A_max)

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    max_a = max(a)
    max_index = a.index(max_a)
    for i in range(n):
        if i == max_index:
            print(max(a[:i] + a[i + 1:]))
        else:
            print(max_a)
