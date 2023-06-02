Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    A = 0
    B = 0
    for i in range(N):
        if A > B:
            B += T[i]
        else:
            A += T[i]
    print(max(A, B))

=======
Suggestion 2

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    t1 = 0
    t2 = 0
    for i in range(N):
        if t1 <= t2:
            t1 += T[N - 1 - i]
        else:
            t2 += T[N - 1 - i]
    print(max(t1, t2))

=======
Suggestion 3

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    a = 0
    b = 0
    for i in range(n):
        if a < b:
            a += t[i]
        else:
            b += t[i]
    print(max(a, b))

=======
Suggestion 4

def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(min2(T))

=======
Suggestion 5

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    T1 = 0
    T2 = 0
    for i in range(N):
        if T1 < T2:
            T1 += T[i]
        else:
            T2 += T[i]
    print(max(T1, T2))

=======
Suggestion 6

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    t1 = 0
    t2 = 0
    for i in range(N):
        if t1 < t2:
            t1 += T[N-i-1]
        else:
            t2 += T[N-i-1]
    print(max(t1, t2))

=======
Suggestion 7

def solve(N, T):
    T.sort()
    T.reverse()
    oven1 = 0
    oven2 = 0
    for i in range(N):
        if oven1 < oven2:
            oven1 += T[i]
        else:
            oven2 += T[i]
    return max(oven1, oven2)

=======
Suggestion 8

def main():
    N = int(input())
    T = [int(i) for i in input().split()]
    T.sort()
    oven = [0] * 2
    for i in range(N):
        oven[0] += T.pop()
        oven.sort()
    print(oven[1])

=======
Suggestion 9

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(T[N-1]+T[N-2])

=======
Suggestion 10

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    print(t[-1] + t[-2])
