Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, W = map(int, input().split())

=======
Suggestion 2

def main():
    N,W = map(int,input().split())
    time = []
    for i in range(N):
        s,t,p = map(int,input().split())
        time.append([s,p])
        time.append([t,-p])
    time.sort()
    water = 0
    for i in range(2*N):
        water += time[i][1]
        if water > W:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n, w = map(int, input().split())
    a = [0] * 200001
    for i in range(n):
        s, t, p = map(int, input().split())
        a[s] += p
        a[t] -= p
    for i in range(1, 200001):
        a[i] += a[i - 1]
        if a[i] > w:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def solve():
    N, W = map(int, input().split())
    events = []

    for i in range(N):
        S, T, P = map(int, input().split())
        events.append((S, P))
        events.append((T, -P))

    events.sort()

    water = 0
    for _, p in events:
        water += p
        if water > W:
            print('No')
            return

    print('Yes')

=======
Suggestion 5

def main():
    n,w = map(int,input().split())
    stp = [list(map(int,input().split())) for _ in range(n)]
    # print(stp)
    # print(n,w)
    # print(stp[0][0])

    # s = [i[0] for i in stp]
    # t = [i[1] for i in stp]
    # p = [i[2] for i in stp]
    # print(s)
    # print(t)
    # print(p)

    # print(s[0])
    # print(t[0])
    # print(p[0])

    # print(stp[0][0])
    # print(stp[0][1])
    # print(stp[0][2])

    # print(stp[0][1] - stp[0][0])
    # print(stp[0][2])

    # print(stp[0][1] - stp[0][0] * stp[0][2])

    # print(stp[0][1] - stp[0][0] * stp[0][2] + stp[1][1] - stp[1][0] * stp[1][2])
    # print(stp[0][1] - stp[0][0] * stp[0][2] + stp[1][1] - stp[1][0] * stp[1][2] + stp[2][1] - stp[2][0] * stp[2][2])
    # print(stp[0][1] - stp[0][0] * stp[0][2] + stp[1][1] - stp[1][0] * stp[1][2] + stp[2][1] - stp[2][0] * stp[2][2] + stp[3][1] - stp[3][0] * stp[3][2])
    # print(stp[0][1] - stp[0][0] * stp[0][2] + stp[1][1] - stp[1][0] * stp[1][2] + stp[2][1] - stp

=======
Suggestion 6

def solve():
    N, W = map(int, input().split())
    S = [0] * N
    T = [0] * N
    P = [0] * N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())

    # 用于计算每一分钟的热水总量
    # 0 代表开始，W 代表结束
    imos = [0] * (2 * 10 ** 5 + 2)
    for i in range(N):
        imos[S[i]] += P[i]
        imos[T[i]] -= P[i]

    # 累积和
    for i in range(2 * 10 ** 5 + 1):
        imos[i + 1] += imos[i]

    # 检查是否超过了W
    for i in range(2 * 10 ** 5 + 1):
        if imos[i] > W:
            print("No")
            return

    print("Yes")

=======
Suggestion 7

def solve():
    N, W = map(int, input().split())
    A = []
    for _ in range(N):
        s, t, p = map(int, input().split())
        A.append((s, p))
        A.append((t, -p))
    A.sort()
    
    cur = 0
    for _, p in A:
        cur += p
        if cur > W:
            print('No')
            return
    print('Yes')

solve()

=======
Suggestion 8

def main():
    n,w = map(int, input().split())
    stp = [list(map(int, input().split())) for _ in range(n)]
    #print(stp)
    # 1.按照开始时间排序
    stp.sort(key=lambda x:x[0])
    #print(stp)
    # 2.按照结束时间排序
    stp.sort(key=lambda x:x[1])
    #print(stp)
    # 3.按照使用量排序
    stp.sort(key=lambda x:x[2], reverse=True)
    #print(stp)
    # 4.按照开始时间排序
    stp.sort(key=lambda x:x[0])
    #print(stp)
    # 5.开始遍历
    w0 = w
    for i in range(n):
        if w0 < stp[i][2]:
            print("No")
            return
        w0 -= stp[i][2]
    print("Yes")

=======
Suggestion 9

def main():
    n, w = map(int, input().split())
    time = [0] * 200005
    for i in range(n):
        s, t, p = map(int, input().split())
        time[s] += p
        time[t] -= p
    for i in range(1, 200005):
        time[i] += time[i - 1]
        if time[i] > w:
            print("No")
            return
    print("Yes")
