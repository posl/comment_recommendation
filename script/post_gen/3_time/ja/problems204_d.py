Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    oven1 = 0
    oven2 = 0
    for i in range(n):
        if oven1 <= oven2:
            oven1 += t[i]
        else:
            oven2 += t[i]
    print(max(oven1, oven2))

=======
Suggestion 2

def main():
    N = int(input())
    T = list(map(int, input().split()))

    T.sort()

    if N == 1:
        print(T[0])
    elif N == 2:
        print(max(T[0], T[1]))
    else:
        T1 = T[0]
        T2 = T[1]
        for i in range(2, N):
            if T1 < T2:
                T1 += T[i]
            else:
                T2 += T[i]
        print(max(T1, T2))

=======
Suggestion 3

def func(n, t):
    if n == 1:
        return t[0]
    if n == 2:
        return max(t[0], t[1])
    if n == 3:
        return max(t[0]+t[1], t[2])
    if n == 4:
        return max(t[0]+t[3], t[1]+t[2])
    if n == 5:
        return max(t[0]+t[3]+t[4], t[1]+t[2]+t[4])
    if n == 6:
        return max(t[0]+t[3]+t[5], t[1]+t[2]+t[5], t[0]+t[1]+t[2]+t[3]+t[4]+t[5])
    if n == 7:
        return max(t[0]+t[3]+t[6], t[1]+t[2]+t[6], t[0]+t[1]+t[2]+t[3]+t[4]+t[6])
    if n == 8:
        return max(t[0]+t[3]+t[7], t[1]+t[2]+t[7], t[0]+t[1]+t[2]+t[3]+t[4]+t[7], t[0]+t[1]+t[2]+t[3]+t[5]+t[6])
    if n == 9:
        return max(t[0]+t[3]+t[8], t[1]+t[2]+t[8], t[0]+t[1]+t[2]+t[3]+t[4]+t[8], t[0]+t[1]+t[2]+t[3]+t[5]+t[8], t[0]+t[1]+t[2]+t[3]+t[6]+t[7])

=======
Suggestion 4

def main():
    N = int(input())
    T = list(map(int, input().split()))

    T.sort()
    t1 = 0
    t2 = 0
    for i in range(N):
        if t1 <= t2:
            t1 += T[N-i-1]
        else:
            t2 += T[N-i-1]
    print(max(t1, t2))

=======
Suggestion 5

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    T1 = 0
    T2 = 0
    for i in range(N):
        if T1 <= T2:
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
    #print(T)
    t1 = 0
    t2 = 0
    for i in range(N):
        if t1 <= t2:
            t1 += T[N-i-1]
        else:
            t2 += T[N-i-1]
    print(max(t1,t2))

=======
Suggestion 7

def main():
    # input
    N = int(input())
    T = list(map(int, input().split()))

    # compute
    ans = 0
    for i in range(N):
        ans += T[i]
    ans = ans - max(T) + max(T)/2

    # output
    print(int(ans))

=======
Suggestion 8

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    #print(t)
    t1 = 0
    t2 = 0
    for i in range(n):
        if t1 < t2:
            t1 += t[-1-i]
        else:
            t2 += t[-1-i]
    print(max(t1, t2))

=======
Suggestion 9

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(T[-1])

=======
Suggestion 10

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    ovens = [0, 0]
    for t in T:
        if ovens[0] < ovens[1]:
            ovens[0] += t
        else:
            ovens[1] += t
    print(max(ovens))
