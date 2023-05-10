Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        ci, ti = map(int, input().split())
        c.append(ci)
        t.append(ti)
    min_cost = 1001
    for i in range(N):
        if t[i] <= T:
            if c[i] < min_cost:
                min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 2

def main():
    n,t = map(int,input().split())
    c = []
    c = [0]*n
    t = [0]*n
    for i in range(n):
        c[i],t[i] = map(int,input().split())
    min_cost = 1001
    for i in range(n):
        if t[i] <= t:
            min_cost = min(min_cost,c[i])
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 3

def main():
    n, t = map(int, input().split())
    min_cost = 1001
    for i in range(n):
        c, tt = map(int, input().split())
        if tt <= t:
            if min_cost > c:
                min_cost = c
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 4

def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    c = sorted(c, key=lambda x: x[0])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            return
    print("TLE")

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    min_cost = 1001
    for i in range(N):
        if t[i] <= T and c[i] < min_cost:
            min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 6

def main():
    n, t = map(int, input().split())
    cost_time = []
    for i in range(n):
        cost, time = map(int, input().split())
        cost_time.append((cost, time))

    cost_time.sort(key=lambda x: x[1])
    for cost, time in cost_time:
        if time <= t:
            print(cost)
            return
    print("TLE")

=======
Suggestion 7

def solve():
    # 入力
    N, T = map(int, input().split())
    routes = []
    for _ in range(N):
        c, t = map(int, input().split())
        routes.append((c, t))

    # 時間 T 以内に帰宅できる経路のうち、コストが最小となる経路のコストを求める
    min_cost = float('inf')
    for c, t in routes:
        if t <= T:
            min_cost = min(min_cost, c)

    # 出力
    if min_cost == float('inf'):
        print('TLE')
    else:
        print(min_cost)

=======
Suggestion 8

def main():
    n,t = map(int,input().split())
    c = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    c.sort(key=lambda x:x[0])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            break
        elif i == n-1:
            print('TLE')

=======
Suggestion 9

def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c_i, t_i = map(int, input().split())
        c.append([c_i, t_i])
    
    c.sort(key=lambda x: x[0])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            return
    print("TLE")

=======
Suggestion 10

def solve():
    n, t = map(int, input().split())
    cost_list = []
    time_list = []
    for i in range(n):
        cost, time = map(int, input().split())
        cost_list.append(cost)
        time_list.append(time)
    cost_list = [cost for (time, cost) in sorted(zip(time_list, cost_list))]
    time_list.sort()
    for i in range(n):
        if time_list[i] <= t:
            print(cost_list[i])
            return
    print("TLE")
