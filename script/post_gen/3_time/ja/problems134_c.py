Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        print(max(a[:i]+a[i+1:]))

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    max1 = max(A)
    max2 = sorted(A)[-2]
    for i in range(N):
        if A[i] == max1:
            print(max2)
        else:
            print(max1)

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    a_max = max(a)
    a_max2 = max(a[:a.index(a_max)] + a[a.index(a_max)+1:])
    for i in range(n):
        if a[i] == a_max:
            print(a_max2)
        else:
            print(a_max)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        max_a = max(a)
        if a[i] == max_a:
            a[i] = max(a[0:i] + a[i+1:n])
        print(a[i])

=======
Suggestion 5

def main():
    n = int(input())
    a = list()
    for i in range(n):
        a.append(int(input()))

    max = 0
    for i in range(n):
        if a[i] > max:
            max = a[i]

    for i in range(n):
        if a[i] == max:
            if i == 0:
                max2 = a[1]
            else:
                max2 = a[0]
            for j in range(n):
                if j != i:
                    if a[j] > max2:
                        max2 = a[j]
            print(max2)
        else:
            print(max)

=======
Suggestion 6

def solve():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_idx = a.index(a_max)
    a.pop(a_max_idx)
    for i in range(n):
        print(a_max if i != a_max_idx else max(a))

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    b = []
    for i in range(n):
        b.append(a[:i] + a[i+1:])
    for i in range(n):
        print(max(b[i]))

=======
Suggestion 8

def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    max_value = a[-1]
    for i in range(n):
        if a[i] == max_value:
            print(a[-2])
        else:
            print(max_value)

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    max_a = max(a)
    max_a2 = max(a)
    for i in a:
        if i == max_a:
            max_a2 = max(a)
            print(max_a2)
        else:
            print(max_a)
