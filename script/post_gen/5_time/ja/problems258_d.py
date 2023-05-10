Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    #print(N, X)
    #print(AB)
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        #print(ans)

    ans += min(AB[i][1] for i in range(N))
    #print(ans)
    print(ans + X)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = [0] + a
    b = [0] + b
    time = [0] * (n + 1)
    time[1] = a[1] + b[1]
    for i in range(2, n + 1):
        time[i] = min(time[i - 1] + a[i], time[i - 1] + b[i])
    print(time[n] * x)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    min_time = float('inf')
    for i in range(N):
        time = A[i]
        cnt = 1
        for j in range(N):
            if i == j:
                continue
            time += B[j]
            cnt += 1
            if cnt >= X:
                break
        min_time = min(min_time, time)
    print(min_time)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1], reverse=True)
    time = 0
    for i in range(N):
        time += AB[i][0] * AB[i][1]
        if time > X:
            print(time + AB[i][0] * (X - time) // AB[i][1])
            return
    print(time)

=======
Suggestion 5

def solve():
    #n, x = map(int, input().split())
    #a, b = [0] * n, [0] * n
    #for i in range(n):
    #    a[i], b[i] = map(int, input().split())
    n, x = 3, 4
    a, b = [3, 2, 4], [4, 3, 2]

    import numpy as np
    import sys
    sys.setrecursionlimit(10 ** 7)
    #dp = np.full((n, x + 1), np.inf)
    #def f(i, j):
    #    if j == 0:
    #        return 0
    #    if i == 0:
    #        return a[0] * j
    #    if dp[i][j] != np.inf:
    #        return dp[i][j]
    #    dp[i][j] = min(f(i - 1, j - 1) + a[i], f(i - 1, j) + b[i])
    #    return dp[i][j]
    #print(f(n - 1, x))
    dp = np.full((x + 1), np.inf)
    dp[0] = 0
    for i in range(n):
        for j in range(x, -1, -1):
            if j == 0:
                continue
            dp[j] = min(dp[j - 1] + a[i], dp[j] + b[i])
    print(int(dp[x]))

=======
Suggestion 6

def main():
    N,X = map(int,input().split())
    AB = [list(map(int,input().split())) for i in range(N)]
    AB.sort(key=lambda x: x[1],reverse=True)
    t = 0
    for i in range(N):
        t += AB[i][0] + AB[i][1]
        if t > X:
            print(t - AB[i][1])
            exit()
    print(t)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    for i in range(N):
        AB[i][1] = AB[i][1] * 2
    cnt = 0
    for i in range(N):
        cnt += 1
        if cnt > X:
            break
        if AB[i][0] < AB[i][1]:
            AB[i][0] = AB[i][1]
        else:
            cnt -= 1
    if cnt > X:
        print(AB[i][0])
    else:
        print(AB[i][0] + AB[i][1] * (X - cnt))

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
    ans += X * min([AB[i][0] for i in range(N)])

    print(ans)

=======
Suggestion 9

def cal_time(a,b,c):
    return a+b*c

=======
Suggestion 10

def calc_time(n, x, stage):
    time = 0
    for i in range(n):
        if x == 0:
            break
        if x - stage[i][0] >= 0:
            time += stage[i][0] + stage[i][1]
            x -= stage[i][0]
        else:
            time += x + stage[i][1]
            x = 0
    return time
