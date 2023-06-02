Synthesizing 10/10 solutions

=======
Suggestion 1

def process(n, s, t):
    times = [0] * n
    for i in range(n):
        times[i] = t[i]
        if i == 0:
            times[i] = max(times[i], s[i])
        else:
            times[i] = max(times[i], times[i - 1] + s[i])
    return times

=======
Suggestion 2

def main():
    N = int(input())
    S = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]
    res = [0 for i in range(N)]
    res[0] = T[0]
    for i in range(1, N):
        if res[i-1] + S[i-1] < T[i]:
            res[i] = T[i]
        else:
            res[i] = res[i-1] + S[i-1]
    for i in range(N):
        print(res[i])

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(1, N):
        ans[i] = min(ans[i], ans[i - 1] + S[i - 1])
    ans[0] = min(ans[0], ans[N - 1] + S[N - 1])

    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    for i in range(n):
        t[i] = (t[i], i)
    t.sort()
    ans = [0] * n
    for i in range(n):
        ans[t[i][1]] = t[i][0]
    for i in range(n):
        if ans[i] < s[i]:
            ans[i] = s[i]
        elif ans[i] % s[i] == 0:
            pass
        else:
            ans[i] = s[i] * (ans[i] // s[i] + 1)
    for i in range(n):
        print(ans[i])

=======
Suggestion 5

def solve():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(1, N):
        ans[i] = min(ans[i], ans[i - 1] + S[i - 1])
    for i in range(N):
        ans[i] = min(ans[i], ans[(i - 1 + N) % N] + S[(i - 1 + N) % N])
    for i in range(N):
        print(ans[i])

=======
Suggestion 6

def solve():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s_t = sorted(zip(s, t), key=lambda x: x[0])
    s, t = zip(*s_t)
    ans = [0] * n
    ans[0] = t[0]
    for i in range(1, n):
        ans[i] = min(ans[i - 1] + s[i - 1], t[i])
    for i in range(n):
        print(ans[i])

=======
Suggestion 7

def solve(N, S, T):
    # 用于存储Snuke i第一次收到宝石的时间
    ans = [0] * N
    # 用于存储Snuke i第一次收到宝石的时间的最小值
    min_time = 0
    # 用于存储Snuke i第一次收到宝石的时间的最大值
    max_time = 0
    # 用于存储Snuke i第一次收到宝石的时间的最大值的索引
    max_time_index = 0
    # 用于存储Snuke i第一次收到宝石的时间的最小值的索引
    min_time_index = 0
    # 用于存储Snuke i第一次收到宝石的时间的最小值的索引
    min_time_index = 0
    # 用于存储Snuke i第一次收到宝石的时间的最大值的索引
    max_time_index = 0
    # 用于存储Snuke i第一次收到宝石

=======
Suggestion 8

def main():
    n = int(input())
    snuke = list(map(int, input().split()))
    takahashi = list(map(int, input().split()))

    snuke_time = [0] * n
    snuke_time[0] = takahashi[0]
    for i in range(1, n):
        snuke_time[i] = max(snuke_time[i - 1] + snuke[i - 1], takahashi[i])

    for i in range(n):
        print(snuke_time[i])

=======
Suggestion 9

def main():
    #N = 3
    #S = [4, 1, 5]
    #T = [3, 10, 100]
    #N = 4
    #S = [100, 100, 100, 100]
    #T = [1, 1, 1, 1]
    #N = 4
    #S = [1, 2, 3, 4]
    #T = [1, 2, 4, 7]
    N = 8
    S = [84, 87, 78, 16, 94, 36, 87, 93]
    T = [50, 22, 63, 28, 91, 60, 64, 27]
    #print(N, S, T)
    #N = int(input())
    #S = list(map(int, input().split()))
    #T = list(map(int, input().split()))
    #print(N, S, T)

    #print(S[0], T[0])
    #print(S[1], T[1])
    #print(S[2], T[2])

    #print(S[0], T[0])
    #print(S[1], T[1])
    #print(S[2], T[2])
    #print(S[3], T[3])

    #print(S[0], T[0])
    #print(S[1], T[1])
    #print(S[2], T[2])
    #print(S[3], T[3])
    #print(S[4], T[4])

    #print(S[0], T[0])
    #print(S[1], T[1])
    #print(S[2], T[2])
    #print(S[3], T[3])
    #print(S[4], T[4])
    #print(S[5], T[5])

    #print(S[0], T[0])
    #print(S[1], T[1])
    #print(S[2], T[2])
    #print(S[3], T[3])
    #print(S[4], T[4])
    #print(S[5], T[5])
    #print(S[6], T[6])

    #print

=======
Suggestion 10

def main():
    N = int(input())
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))
    for i in range(N):
        T[i] = [T[i],i]
    T.sort()
    for i in range(N):
        T[i] = T[i][1]
    for i in range(N):
        if i == 0:
            time = 0
        else:
            time = max(time,S[T[i-1]])
        print(time)
