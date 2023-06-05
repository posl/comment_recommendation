Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    print(sum(t[:-1])+t[-1]//2)

=======
Suggestion 2

def main():
    n = int(input())
    t = list(map(int,input().split()))
    t.sort()
    print(t[-1]+t[-2])

=======
Suggestion 3

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    ans = 0
    for i in range(n):
        ans = max(ans, sum(t[:i+1]) + t[i]//2)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort(reverse=True)

    a, b = 0, 0
    for i in range(n):
        if a < b:
            a += t[i]
        else:
            b += t[i]

    print(max(a, b))

=======
Suggestion 5

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    t1 = T.pop()
    t2 = T.pop()
    while T:
        if t1 < t2:
            t1 += T.pop()
        else:
            t2 += T.pop()
    print(max(t1, t2))

=======
Suggestion 6

def cooking_time(N, T):
    if N == 1:
        return T[0]
    elif N == 2:
        return max(T[0], T[1])
    else:
        T = sorted(T)
        t1 = T.pop()
        t2 = T.pop()
        t3 = T.pop()
        if t1 + t3 > t2 + t2:
            T.append(t1)
            T.append(t3)
            return t2 + cooking_time(N - 2, T)
        else:
            T.append(t1)
            T.append(t2)
            return t1 + cooking_time(N - 1, T)

=======
Suggestion 7

def solve(n, t):
    t.sort()
    if n == 1:
        return t[0]
    elif n == 2:
        return max(t)
    else:
        t1 = t.pop()
        t2 = t.pop()
        t3 = t.pop()
        t4 = t.pop()
        return t1 + min(t2, t3, t4) + solve(n - 1, t)

=======
Suggestion 8

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    if N == 1:
        print(T[0])
        return
    if N == 2:
        print(max(T[0], T[1]))
        return
    if N == 3:
        print(max(T[0] + T[1], T[2]))
        return
    if N == 4:
        print(max(T[0] + T[3], T[1] + T[2]))
        return
    if N == 5:
        print(max(T[0] + T[3] + T[4], T[1] + T[2] + T[4]))
        return
    if N == 6:
        print(max(T[0] + T[3] + T[4] + T[5], T[1] + T[2] + T[4] + T[5]))
        return
    if N == 7:
        print(max(T[0] + T[3] + T[4] + T[5] + T[6], T[1] + T[2] + T[4] + T[5] + T[6]))
        return
    if N == 8:
        print(max(T[0] + T[3] + T[4] + T[5] + T[6] + T[7], T[1] + T[2] + T[4] + T[5] + T[6] + T[7]))
        return
    if N == 9:
        print(max(T[0] + T[3] + T[4] + T[5] + T[6] + T[7] + T[8], T[1] + T[2] + T[4] + T[5] + T[6] + T[7] + T[8]))
        return
    if N == 10:
        print(max(T[0] + T[3] + T[4] + T[5] + T[6] + T[7] + T[8] + T[9],
                  T[1] + T[2] + T[4] + T[5] + T[6] + T[7

=======
Suggestion 9

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    if n == 2:
        print(t[1])
    else:
        t1 = t[n - 1]
        t2 = t[n - 2]
        for i in range(n - 3, -1, -1):
            if t1 <= t2:
                t1 += t[i]
            else:
                t2 += t[i]
        print(max(t1, t2))

=======
Suggestion 10

def solve(n, t):
    if n == 1:
        return t[0]
    if n == 2:
        return max(t[0], t[1])
    if n == 3:
        return min(max(t[0], t[1]), t[2])
    if n == 4:
        return min(max(t[0], t[1]) + max(t[2], t[3]), min(max(t[0], t[2]) + max(t[1], t[3]), max(t[0], t[3]) + max(t[1], t[2])))
    if n == 5:
        return min(max(t[0], t[1]) + max(t[2], t[3]) + t[4], min(max(t[0], t[2]) + max(t[1], t[3]) + t[4], max(t[0], t[3]) + max(t[1], t[2]) + t[4], min(max(t[0], t[1]) + t[2] + t[3], max(t[0], t[2]) + t[1] + t[3], max(t[0], t[3]) + t[1] + t[2])))
    if n == 6:
        return min(max(t[0], t[1]) + max(t[2], t[3]) + max(t[4], t[5]), min(max(t[0], t[2]) + max(t[1], t[3]) + max(t[4], t[5]), max(t[0], t[3]) + max(t[1], t[2]) + max(t[4], t[5]), min(max(t[0], t[1]) + max(t[2], t[4]) + t[3], max(t[0], t[1]) + max(t[2], t[5]) + t[3], max(t[0], t[1]) + max(t[3], t[4]) + t[2], max(t[0], t[1]) + max(t[3], t[5]) + t[2], max(t[0], t[1]) + max(t[4], t[5]) + t[2], max(t[0], t[2]) + max(t[
