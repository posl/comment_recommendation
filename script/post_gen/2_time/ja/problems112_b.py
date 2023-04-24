Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    ans = 1001
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    if ans == 1001:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for _ in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    #print(c)
    #print(t)
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
Suggestion 3

def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for _ in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)

    cost = 1001
    for i in range(N):
        if t[i] <= T:
            cost = min(cost, c[i])

    if cost == 1001:
        print('TLE')
    else:
        print(cost)

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    costs = []
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T:
            costs.append(c)
    if len(costs) == 0:
        print("TLE")
    else:
        print(min(costs))

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    min_cost = 1001
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T:
            min_cost = min(min_cost, c)
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 6

def main():
    n, t = map(int, input().split())
    ans = 1000
    for i in range(n):
        c, ti = map(int, input().split())
        if ti <= t:
            ans = min(ans, c)
    if ans == 1000:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 7

def main():
    N, T = map(int, input().split())
    #print(N, T)
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    #print(c, t)
    ans = 10000
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    if ans == 10000:
        print('TLE')
    else:
        print(ans)

=======
Suggestion 8

def main():
    # 標準入力から N, T を取得
    N, T = map(int, input().split())
    # 標準入力から N 個の経路を取得し、リストに格納
    routes = [list(map(int, input().split())) for _ in range(N)]
    # 最小コストを格納する変数
    min_cost = float("inf")
    # 経路を1つずつ取り出す
    for route in routes:
        # 経路のコストと時間を取得
        cost, time = route
        # 経路の時間が T 以内であれば
        if time <= T:
            # 経路のコストを最小コストと比較し、もし経路のコストが小さければ
            if cost < min_cost:
                # 最小コストを更新
                min_cost = cost
    # 最小コストが更新されていれば
    if min_cost != float("inf"):
        # 最小コストを出力
        print(min_cost)
    # 最小コストが更新されていなければ
    else:
        # TLE を出力
        print("TLE")

=======
Suggestion 9

def main():
    N, T = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort(key=lambda x: x[0])
    ans = 1001
    for i in range(N):
        if A[i][1] <= T:
            ans = min(ans, A[i][0])
    if ans == 1001:
        print('TLE')
    else:
        print(ans)

=======
Suggestion 10

def main():
    #入力
    N, T = map(int, input().split())
    c_t_list = [list(map(int, input().split())) for _ in range(N)]

    #処理
    c_t_list.sort(key=lambda x: x[1])
    ans = 1001
    for c_t in c_t_list:
        if c_t[1] <= T:
            ans = min(ans, c_t[0])

    #出力
    if ans == 1001:
        print("TLE")
    else:
        print(ans)
