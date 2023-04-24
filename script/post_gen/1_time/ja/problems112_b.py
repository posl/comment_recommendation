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
    cost = 1001
    for i in range(N):
        if t[i] <= T and c[i] < cost:
            cost = c[i]
    if cost == 1001:
        print("TLE")
    else:
        print(cost)

=======
Suggestion 2

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
        if t[i] <= T:
            if c[i] < min_cost:
                min_cost = c[i]

    if min_cost == 1000:
        print('TLE')
    else:
        print(min_cost)

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    cost = 1000
    for i in range(N):
        if t[i] <= T:
            if c[i] < cost:
                cost = c[i]
    if cost == 1000:
        print('TLE')
    else:
        print(cost)

=======
Suggestion 4

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
        if t[i] <= T:
            if c[i] < min_cost:
                min_cost = c[i]
    if min_cost == 1000:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    cost = []
    time = []
    for i in range(N):
        c, t = map(int, input().split())
        cost.append(c)
        time.append(t)
    ans = 1001
    for i in range(N):
        if time[i] <= T:
            ans = min(ans, cost[i])
    if ans == 1001:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 6

def main():
    N, T = map(int, input().split())
    c = [0 for i in range(N)]
    t = [0 for i in range(N)]
    for i in range(N):
        c[i], t[i] = map(int, input().split())
    min_c = 1000000000
    for i in range(N):
        if t[i] <= T:
            if c[i] < min_c:
                min_c = c[i]
    if min_c == 1000000000:
        print("TLE")
    else:
        print(min_c)

=======
Suggestion 7

def main():
    # 入力
    N, T = map(int, input().split())
    c = [0] * N
    t = [0] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())
    # 処理
    ans = 1001
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    # 出力
    if ans != 1001:
        print(ans)
    else:
        print("TLE")

=======
Suggestion 8

def main():
    n, t = map(int, input().split())
    ans = 1001
    for i in range(n):
        c, tt = map(int, input().split())
        if tt <= t:
            ans = min(ans, c)
    if ans == 1001:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 9

def main():
    N,T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    ans = 1000000
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    if ans == 1000000:
        print('TLE')
    else:
        print(ans)

=======
Suggestion 10

def main():
    # 標準入力から N, T を取得
    N, T = map(int, input().split())

    # 標準入力から N 個の (c_i, t_i) を取得
    routes = [tuple(map(int, input().split())) for _ in range(N)]

    # コストが最小となる経路のコストを求める
    # 時間 T 以内に帰宅できる経路のうち、コストが最小となる経路のコストを求める
    # ただし、どの経路を使っても時間 T 以内に帰宅できない場合、TLE と出力せよ。
    min_cost = min([c for c, t in routes if t <= T], default="TLE")

    # コストが最小となる経路のコストを出力
    print(min_cost)
