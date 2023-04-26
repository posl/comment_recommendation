Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    min_cost = 1000
    for i in range(N):
        if t[i] <= T and c[i] < min_cost:
            min_cost = c[i]
    if min_cost == 1000:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 2

def main():
    n, t = map(int, input().split())
    c = [0] * n
    time = [0] * n
    for i in range(n):
        c[i], time[i] = map(int, input().split())
    ans = 1001
    for i in range(n):
        if time[i] <= t:
            ans = min(ans, c[i])
    if ans == 1001:
        print('TLE')
    else:
        print(ans)

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    min_cost = 1001
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T and c < min_cost:
            min_cost = c
    if min_cost == 1001:
        print('TLE')
    else:
        print(min_cost)

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    C = []
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            C.append(c)
    if len(C) == 0:
        print("TLE")
    else:
        print(min(C))

=======
Suggestion 5

def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        ci, ti = map(int, input().split())
        if ti <= t:
            c.append(ci)
    if len(c) == 0:
        print("TLE")
    else:
        print(min(c))

=======
Suggestion 6

def main():
    n, t = map(int, input().split())
    min_c = 1000
    for _ in range(n):
        c, time = map(int, input().split())
        if time <= t:
            min_c = min(min_c, c)
    if min_c == 1000:
        print("TLE")
    else:
        print(min_c)

=======
Suggestion 7

def main():
    # 標準入力から N と T を取得する
    n, t = map(int, input().split())

    # N 個の帰宅経路を取得する
    c = []
    t = []
    for i in range(n):
        c_tmp, t_tmp = map(int, input().split())
        c.append(c_tmp)
        t.append(t_tmp)

    # コストが最小となる経路のコストを求める
    # ただし、どの経路を使っても時間 T 以内に帰宅できない場合、TLE と出力する
    cost = 1001
    for i in range(n):
        if t[i] <= t:
            if cost > c[i]:
                cost = c[i]
    if cost == 1001:
        print('TLE')
    else:
        print(cost)

=======
Suggestion 8

def main():
    n, t = map(int,input().split())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:x[0])
    for i in range(n):
        if l[i][1] <= t:
            print(l[i][0])
            exit()
    print("TLE")

=======
Suggestion 9

def mincost():
    n, t = map(int, input().split())
    cost = [0] * n
    time = [0] * n
    for i in range(n):
        cost[i], time[i] = map(int, input().split())

    min_cost = 1001
    for i in range(n):
        if time[i] <= t:
            if cost[i] < min_cost:
                min_cost = cost[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 10

def main():
    # データ入力
    n, t = map(int, input().split())

    # データ入力
    cost = []
    time = []
    for i in range(n):
        c, ti = map(int, input().split())
        cost.append(c)
        time.append(ti)

    # 初期化
    min_cost = 1000

    # 計算
    for i in range(n):
        if time[i] <= t:
            if cost[i] < min_cost:
                min_cost = cost[i]

    # 出力
    if min_cost == 1000:
        print("TLE")
    else:
        print(min_cost)
