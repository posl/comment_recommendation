Synthesizing 10/10 solutions

=======
Suggestion 1

def search_route(routes, T):
    routes = sorted(routes, key=lambda x: x[0])
    routes = sorted(routes, key=lambda x: x[1])
    print(routes)

    cost = 0
    for route in routes:
        if route[1] <= T:
            cost = route[0]
            break
    return cost

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    c_t = []
    for i in range(N):
        c_t.append(list(map(int, input().split())))
    c_t.sort(key=lambda x:x[1])
    for i in range(N):
        if c_t[i][1] <= T:
            print(c_t[i][0])
            return
    print("TLE")

=======
Suggestion 3

def main():
    n, t = map(int, input().split())
    cost = []
    time = []
    for i in range(n):
        c, ti = map(int, input().split())
        cost.append(c)
        time.append(ti)
    min_cost = 1000
    for i in range(n):
        if time[i] <= t:
            if cost[i] < min_cost:
                min_cost = cost[i]
    if min_cost == 1000:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 4

def input():
    # 读取输入
    # 读取整数n和t
    line = input().split()
    n = int(line[0])
    t = int(line[1])
    # 读取n行
    routes = []
    for i in range(n):
        line = input().split()
        routes.append([int(line[0]), int(line[1])])
    return n, t, routes

=======
Suggestion 5

def get_input():
    N,T = [int(i) for i in input().split()]
    c_t = []
    for i in range(N):
        c_t.append([int(i) for i in input().split()])
    return N,T,c_t

=======
Suggestion 6

def solve():
    # 读取输入
    N, T = map(int, input().split())
    routes = []
    for i in range(N):
        c, t = map(int, input().split())
        routes.append((c, t))
    # 计算最小花费
    min_cost = float('inf')
    for c, t in routes:
        if t <= T:
            min_cost = min(c, min_cost)
    # 输出结果
    if min_cost == float('inf'):
        print('TLE')
    else:
        print(min_cost)

=======
Suggestion 7

def solve():
    N, T = map(int, input().split())
    c = []
    t = []
    for _ in range(N):
        ci, ti = map(int, input().split())
        c.append(ci)
        t.append(ti)

    min_cost = 1001
    for i in range(N):
        if t[i] <= T and c[i] < min_cost:
            min_cost = c[i]

    if min_cost == 1001:
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
    for i in c:
        if i[1] <= t:
            print(i[0])
            break
    else:
        print("TLE")

=======
Suggestion 9

def main():
    n,t = map(int,input().split())
    c = []
    time = []
    for i in range(n):
        c_time = list(map(int,input().split()))
        c.append(c_time[0])
        time.append(c_time[1])
    min_cost = 1001
    for i in range(n):
        if time[i] <= t:
            if c[i] < min_cost:
                min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 10

def main():
    n,t = map(int,input().split())
    c = []
    T = []
    for i in range(n):
        c_i,t_i = map(int,input().split())
        c.append(c_i)
        T.append(t_i)
    c_min = 1000
    for i in range(n):
        if T[i] <= t:
            if c[i] < c_min:
                c_min = c[i]
    if c_min == 1000:
        print("TLE")
    else:
        print(c_min)
