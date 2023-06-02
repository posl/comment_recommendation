Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a_list = []
    for i in range(n):
        a_list.append(int(input()))
    for i in range(n):
        print(max(a_list[:i] + a_list[i+1:]))

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A_max = max(A)
    A_max2 = sorted(A)[-2]
    for i in range(N):
        if A[i] == A_max:
            print(A_max2)
        else:
            print(A_max)

=======
Suggestion 3

def max_without_index(arr, index):
    arr.pop(index)
    return max(arr)

N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

for i in range(N):
    print(max_without_index(A[:], i))

=======
Suggestion 4

def max(a, b):
    if a > b:
        return a
    else:
        return b

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    for i in range(N):
        print(max(A[:i] + A[i+1:]))

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    for i in range(n):
        if a[i] == a_max:
            print(max(a[:i] + a[i+1:]))
        else:
            print(a_max)

=======
Suggestion 7

def problems134_c():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        print(max(a[:i]+a[i+1:]))

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    for i in range(N):
        print(max(A[:i]+A[i+1:]))

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max1 = max(A)
    max2 = sorted(A)[-2]
    for a in A:
        if a == max1:
            print(max2)
        else:
            print(max1)

=======
Suggestion 10

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    max = max(A)
    for i in range(N):
        if A[i] == max:
            print(max(A[:i]+A[i+1:]))
        else:
            print(max)
