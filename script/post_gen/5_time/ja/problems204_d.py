Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    #print(T)
    time1 = 0
    time2 = 0
    for i in range(N):
        if time1 > time2:
            time2 += T[i]
        else:
            time1 += T[i]
    print(max(time1, time2))

=======
Suggestion 2

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    t.reverse()
    t1 = 0
    t2 = 0
    for i in range(n):
        if t1 < t2:
            t1 += t[i]
        else:
            t2 += t[i]
    print(max(t1, t2))

=======
Suggestion 3

def main():
    N = int(input())
    T = [int(i) for i in input().split()]
    T.sort()
    #print(T)
    ans = 0
    ans2 = 0
    ans3 = 0
    ans4 = 0
    ans5 = 0
    ans6 = 0
    ans7 = 0
    ans8 = 0
    ans9 = 0
    for i in range(N):
        if i % 9 == 0:
            ans += T[i]
        elif i % 9 == 1:
            ans2 += T[i]
        elif i % 9 == 2:
            ans3 += T[i]
        elif i % 9 == 3:
            ans4 += T[i]
        elif i % 9 == 4:
            ans5 += T[i]
        elif i % 9 == 5:
            ans6 += T[i]
        elif i % 9 == 6:
            ans7 += T[i]
        elif i % 9 == 7:
            ans8 += T[i]
        elif i % 9 == 8:
            ans9 += T[i]
    print(max(ans, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9))

=======
Suggestion 4

def main():
    n = int(input())
    t = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans = max(ans, t[i])

    print(ans)

=======
Suggestion 5

def solve(n, t):
    t.sort(reverse=True)
    oven1 = 0
    oven2 = 0
    for i in range(n):
        if oven1 <= oven2:
            oven1 += t[i]
        else:
            oven2 += t[i]
    return max(oven1, oven2)

=======
Suggestion 6

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = T[-1]
    for i in range(N-1):
        ans += T[i]
    print(ans)

=======
Suggestion 7

def solve(n, t):
    t.sort()
    t.reverse()
    a = 0
    b = 0
    for i in range(n):
        if a > b:
            b += t[i]
        else:
            a += t[i]
    return max(a, b)

=======
Suggestion 8

def solve():
    N = int(input())
    T = list(map(int, input().split()))

    if N == 1:
        print(T[0])
        return

    if N == 2:
        print(max(T[0], T[1]))
        return

    if N == 3:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[0]))
        return

    if N == 4:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[0]))
        return

    if N == 5:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[0]))
        return

    if N == 6:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[5], T[5] + T[0]))
        return

    if N == 7:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[5], T[5] + T[6], T[6] + T[0]))
        return

    if N == 8:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[5], T[5] + T[6], T[6] + T[7], T[7] + T[0]))
        return

    if N == 9:
        print(max(T[0] + T[1], T[1] + T[2], T[2] + T[3], T[3] + T[4], T[4] + T[5], T[5] + T[6], T[6] +

=======
Suggestion 9

def main():
    # input
    n = int(input())
    t = list(map(int, input().split()))

    # compute
    if n == 1:
        ans = t[0]
    elif n == 2:
        if t[0] < t[1]:
            ans = t[1]
        else:
            ans = t[0]
    else:
        t.sort()
        ans = t[-1]

        for i in range(n-2):
            ans += t[i]

    # output
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    T1 = []
    T2 = []
    for i in range(N):
        if sum(T1) <= sum(T2):
            T1.append(T[i])
        else:
            T2.append(T[i])
    print(max(sum(T1), sum(T2)))
