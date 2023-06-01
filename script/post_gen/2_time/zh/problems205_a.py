Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    print(t[-1] + t[-2])

=======
Suggestion 2

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    t.reverse()
    a = 0
    b = 0
    for i in range(n):
        if a < b:
            a += t[i]
        else:
            b += t[i]
    print(max(a, b))

=======
Suggestion 3

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    t.reverse()
    oven1 = 0
    oven2 = 0
    for i in range(n):
        if oven1 < oven2:
            oven1 += t[i]
        else:
            oven2 += t[i]
    print(max(oven1, oven2))

=======
Suggestion 4

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    a = T[0]
    b = 0
    for i in range(1, N):
        if a > b:
            b += T[i]
        else:
            a += T[i]
    print(max(a, b))

=======
Suggestion 5

def solve(n, t):
    t.sort()
    t.reverse()
    t1 = 0
    t2 = 0
    for i in range(n):
        if t1 < t2:
            t1 += t[i]
        else:
            t2 += t[i]
    return max(t1, t2)

n = int(input())
t = list(map(int, input().split()))
print(solve(n, t))

=======
Suggestion 6

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    t.reverse()
    t1 = 0
    t2 = 0
    for i in range(n):
        if t1 <= t2:
            t1 += t[i]
        else:
            t2 += t[i]
    print(max(t1, t2))

=======
Suggestion 7

def solve():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    t1 = 0
    t2 = 0
    for i in range(N):
        if t1 <= t2:
            t1 += T[i]
        else:
            t2 += T[i]
    print(max(t1, t2))

=======
Suggestion 8

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    #print(T)
    A = T[0]
    B = 0
    for i in range(1, N):
        if A < B:
            A += T[i]
        else:
            B += T[i]
    print(max(A, B))

=======
Suggestion 9

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    t1 = T.pop()
    t2 = 0
    while len(T) > 0:
        if t1 < t2:
            t1 += T.pop()
        else:
            t2 += T.pop()
    print(max(t1, t2))

main()

=======
Suggestion 10

def main():
    n = int(input())
    t = [int(i) for i in input().split()]
    t.sort()
    if n == 1:
        print(t[0])
        return
    if n == 2:
        print(max(t))
        return
    if n == 3:
        print(max(t[0] + t[1], t[2]))
        return
    if n == 4:
        print(max(t[0] + t[3], t[1] + t[2]))
        return
    if n == 5:
        print(max(t[0] + t[4], t[1] + t[3], t[2]))
        return
    if n == 6:
        print(max(t[0] + t[5], t[1] + t[4], t[2] + t[3]))
        return
    if n == 7:
        print(max(t[0] + t[6], t[1] + t[5], t[2] + t[4], t[3]))
        return
    if n == 8:
        print(max(t[0] + t[7], t[1] + t[6], t[2] + t[5], t[3] + t[4]))
        return
    if n == 9:
        print(max(t[0] + t[8], t[1] + t[7], t[2] + t[6], t[3] + t[5], t[4]))
        return
