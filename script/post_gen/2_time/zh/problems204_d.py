Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = 0
    for i in range(N):
        ans += T[i] * (N - i)
    print(ans)

=======
Suggestion 2

def main():
    # 读取输入
    N = int(input())
    T = list(map(int, input().split()))
    # 通过排序，从大到小排列
    T.sort(reverse=True)
    # 用两个烤箱
    oven1 = 0
    oven2 = 0
    for i in range(N):
        if oven1 < oven2:
            oven1 += T[i]
        else:
            oven2 += T[i]
    print(max(oven1, oven2))

=======
Suggestion 3

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    t1 = 0
    t2 = 0
    for i in range(N):
        if t1 <= t2:
            t1 += T[i]
        else:
            t2 += T[i]
    print(max(t1, t2))

=======
Suggestion 4

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
        print(max(T[0] + T[5] + T[4], T[1] + T[2] + T[3]))
        return

    if N == 7:
        print(max(T[0] + T[1] + T[6] + T[5], T[0] + T[2] + T[3] + T[4]))
        return

    if N == 8:
        print(max(T[0] + T[1] + T[6] + T[7], T[0] + T[2] + T[3] + T[4], T[0] + T[1] + T[2] + T[5]))
        return

    if N == 9:
        print(max(T[0] + T[1] + T[2] + T[3] + T[7] + T[8], T[0] + T[1] + T[2] + T[4] + T[5] + T[8], T[0] + T[1] + T[2] + T[4] + T[6] + T[7]))
        return

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
    n = int(input())
    t = list(map(int, input().split()))

    if n == 1:
        print(t[0])
        return

    if n == 2:
        print(max(t))
        return

    t.sort(reverse=True)
    a = t[0]
    b = t[1]
    for i in range(2, n):
        if a > b:
            b += t[i]
        else:
            a += t[i]
    print(max(a, b))

=======
Suggestion 7

def solve(n, t):
    if n == 1:
        return t[0]
    elif n == 2:
        return max(t[0], t[1])
    else:
        return max(t[0] + solve(n-1, t[1:]), t[-1] + solve(n-1, t[:-1]))

=======
Suggestion 8

def get_input():
    #get N
    N = int(input())
    #get T_i
    T_i = list(map(int, input().split()))
    return N, T_i

=======
Suggestion 9

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
Suggestion 10

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    print(t[-1] + sum(t[:-1]) // 2)
