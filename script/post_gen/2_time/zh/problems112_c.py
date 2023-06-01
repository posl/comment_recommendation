Synthesizing 10/10 solutions

=======
Suggestion 1

def search(cost, time, i, t):
    if i == 0:
        return 0
    elif time[i] > t:
        return search(cost, time, i-1, t)
    else:
        return max(search(cost, time, i-1, t), search(cost, time, i-1, t-time[i])+cost[i])

=======
Suggestion 2

def main():
    n, t = map(int, input().split())
    c = []
    for _ in range(n):
        c_i, t_i = map(int, input().split())
        if t_i <= t:
            c.append(c_i)
    if c:
        print(min(c))
    else:
        print("TLE")

=======
Suggestion 3

def find_best_route(N, T, c_list, t_list):
    best_cost = 1001
    for i in range(N):
        if t_list[i] <= T and c_list[i] < best_cost:
            best_cost = c_list[i]
    if best_cost == 1001:
        print("TLE")
    else:
        print(best_cost)

=======
Suggestion 4

def get_input():
    N, T = map(int, input().split())
    c_t = []
    for i in range(N):
        c_t.append(list(map(int, input().split())))
    return N, T, c_t

=======
Suggestion 5

def main():
    # 读取输入
    n, t = map(int, input().split())
    # 读取输入
    lines = []
    for i in range(n):
        c, t = map(int, input().split())
        lines.append((c, t))
    # 找出花费不超过时间T的路线的最小成本
    lines = sorted(lines, key=lambda x: x[0])
    for line in lines:
        if line[1] <= t:
            print(line[0])
            break
    else:
        print('TLE')

=======
Suggestion 6

def getMinCost(n,t,route):
    minCost = 100000
    for i in range(n):
        if route[i][1] <= t:
            if route[i][0] < minCost:
                minCost = route[i][0]
    if minCost == 100000:
        print('TLE')
    else:
        print(minCost)

=======
Suggestion 7

def get_input():
    N, T = map(int, input().split())

    c_list = []
    t_list = []

    for i in range(N):
        c, t = map(int, input().split())
        c_list.append(c)
        t_list.append(t)

    return N, T, c_list, t_list

=======
Suggestion 8

def get_input():
    N,T = map(int,input().split())
    c_t = []
    for _ in range(N):
        c_t.append(list(map(int,input().split())))
    return N,T,c_t

=======
Suggestion 9

def func():
    N, T = map(int, input().split())
    cost_time = []
    for i in range(N):
        cost, time = map(int, input().split())
        if time <= T:
            cost_time.append([cost, time])
    if len(cost_time) == 0:
        print("TLE")
    else:
        cost_time.sort(key=lambda x: x[0])
        print(cost_time[0][0])

=======
Suggestion 10

def main():
    N,T = map(int,input().split())
    c = []
    t = []
    for i in range(N):
        a,b = map(int,input().split())
        c.append(a)
        t.append(b)
    if max(t) > T:
        print('TLE')
    else:
        print(min(c))
