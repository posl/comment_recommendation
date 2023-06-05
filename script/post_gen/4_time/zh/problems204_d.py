Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    t1 = t2 = 0
    for i in range(N):
        if t1 < t2:
            t1 += T[i]
        else:
            t2 += T[i]
    print(max(t1, t2))

=======
Suggestion 2

def solve(n, ti):
    if n == 1:
        return ti[0]
    elif n == 2:
        return max(ti[0], ti[1])
    elif n == 3:
        return max(ti[0]+ti[1], ti[2])
    elif n == 4:
        return max(ti[0]+ti[1], ti[2]+ti[3])
    elif n == 5:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3])
    elif n == 6:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3])
    elif n == 7:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3], ti[0]+ti[2]+ti[6])
    elif n == 8:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3], ti[0]+ti[2]+ti[6], ti[0]+ti[5]+ti[7])
    elif n == 9:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3], ti[0]+ti[2]+ti[6], ti[0]+ti[5]+ti[7], ti[0]+ti[8]+ti[1])
    elif n == 10:
        return max(ti[0]+ti[1]+ti[4], ti[0]+ti[2]+ti[3], ti[0]+ti[5]+ti[3], ti[0]+ti[2]+ti[6], ti[0]+ti[5]+ti[7], ti[0]+ti[8]+ti[1], ti[0]+ti[8]+ti[9])
    else:
        return 0

n = int(input())
ti = list(map(int, input().split()))
ti.sort(reverse=True)
print(solve(n

=======
Suggestion 3

def solve(N, T):
    if N == 1:
        return T[0]
    if N == 2:
        return max(T[0], T[1])
    if N == 3:
        return max(T[0] + T[1], T[2])
    if N == 4:
        return max(T[0] + T[3], T[1] + T[2])
    if N == 5:
        return max(T[0] + T[3] + T[4], T[1] + T[2] + T[3])

=======
Suggestion 4

def solve(n, t):
    t.sort(reverse=True)
    ans = [0, 0]
    for i in range(n):
        ans[ans[0] > ans[1]] += t[i]
    return max(ans)

n = int(input())
t = list(map(int, input().split()))
print(solve(n, t))

=======
Suggestion 5

def main():
    n = int(input())
    t = list(map(int, input().split()))

    # 递归
    # def f(i, x, y):
    #     if i == n:
    #         return max(x, y)
    #     return min(f(i + 1, x + t[i], y), f(i + 1, x, y + t[i]))
    # print(f(0, 0, 0))

    # 动态规划
    # dp = [[float('inf')] * (sum(t) + 1) for _ in range(n + 1)]
    # dp[0][0] = 0
    # for i in range(n):
    #     for j in range(sum(t) + 1):
    #         if j < t[i]:
    #             dp[i + 1][j] = dp[i][j]
    #         else:
    #             dp[i + 1][j] = min(dp[i][j - t[i]] + t[i], dp[i][j])
    # print(max(dp[n]))

    # 动态规划
    dp = [float('inf')] * (sum(t) + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(sum(t) + 1):
            if j < t[i]:
                continue
            dp[j] = min(dp[j - t[i]] + t[i], dp[j])
    print(max(dp))

=======
Suggestion 6

def main():
    n = int(input())
    t = [int(i) for i in input().split()]
    t.sort()
    print(t[-1] + t[-2])

=======
Suggestion 7

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    print(t[-1]+t[-2])

=======
Suggestion 8

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    t.reverse()
    #print(n)
    #print(t)
    a = 0
    b = 0
    for i in range(n):
        if a < b:
            a += t[i]
        else:
            b += t[i]
    print(max(a, b))

=======
Suggestion 9

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    if n == 1:
        print(t[0])
        return
    if n == 2:
        print(max(t[0], t[1]))
        return
    if n == 3:
        print(max(t[0]+t[1], t[2]))
        return
    if n == 4:
        print(max(t[0]+t[3], t[1]+t[2]))
        return
    if n == 5:
        print(max(t[0]+t[4]+t[3], t[2]+t[1]))
        return
    if n == 6:
        print(max(t[0]+t[5]+t[4], t[1]+t[2]+t[3]))
        return
    if n == 7:
        print(max(t[0]+t[6]+t[5], t[1]+t[2]+t[4], t[3]))
        return
    if n == 8:
        print(max(t[0]+t[7]+t[6], t[1]+t[2]+t[5], t[3]+t[4]))
        return
    if n == 9:
        print(max(t[0]+t[8]+t[7], t[1]+t[2]+t[6], t[3]+t[4]+t[5]))
        return

=======
Suggestion 10

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    if N == 1:
        print(T[0])
    elif N == 2:
        print(max(T[0], T[1]))
    else:
        print(T[N-1] + max(sum(T[:N-2]), T[N-2]))
