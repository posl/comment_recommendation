Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,t = map(int,input().split())
    c = []
    time = []
    for i in range(n):
        ci,ti = map(int,input().split())
        c.append(ci)
        time.append(ti)
    min_cost = t
    for i in range(n):
        if time[i] <= t and c[i] < min_cost:
            min_cost = c[i]
    if min_cost == t:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 2

def main():
    n,t = map(int,input().split())
    c_t = []
    for i in range(n):
        c_t.append(list(map(int,input().split())))
    c_t.sort(key=lambda x:x[1])
    for i in range(n):
        if c_t[i][1] > t:
            c_t.pop(i)
            n -= 1
    if n == 0:
        print('TLE')
    else:
        print(min(c_t,key=lambda x:x[0])[0])

=======
Suggestion 3

def solve(n, t, c, ti):
    cost = []
    for i in range(n):
        if ti[i] <= t:
            cost.append(c[i])
    if len(cost) == 0:
        return "TLE"
    else:
        return min(cost)

=======
Suggestion 4

def selectRoute(N, T, routes):
    minCost = 1001
    for i in range(N):
        if routes[i][1] <= T and routes[i][0] < minCost:
            minCost = routes[i][0]
    if minCost == 1001:
        return "TLE"
    else:
        return minCost

=======
Suggestion 5

def get_input():
    N,T = map(int,input().split())
    routes = []
    for i in range(N):
        c,t = map(int,input().split())
        routes.append((c,t))
    return N,T,routes

=======
Suggestion 6

def main():
    n,t = map(int,input().split())
    c = []
    time = []
    for i in range(n):
        c_i,t_i = map(int,input().split())
        c.append(c_i)
        time.append(t_i)
    cost = []
    for i in range(n):
        if time[i] <= t:
            cost.append(c[i])
    if len(cost) == 0:
        print('TLE')
    else:
        print(min(cost))

=======
Suggestion 7

def main():
    n,t=map(int,input().split())
    l=[]
    for _ in range(n):
        c,t=map(int,input().split())
        if t<=t:
            l.append((c,t))
    if len(l)==0:
        print("TLE")
    else:
        print(min(l)[0])

=======
Suggestion 8

def main():
    n, t = map(int, input().split())
    cost = []
    time = []
    for i in range(n):
        c, ti = map(int, input().split())
        cost.append(c)
        time.append(ti)
    min_cost = 1001
    for i in range(n):
        if time[i] <= t and cost[i] < min_cost:
            min_cost = cost[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 9

def main():
    n, t = map(int, input().split())
    c = []
    time = []
    for _ in range(n):
        c_, t_ = map(int, input().split())
        c.append(c_)
        time.append(t_)

    min_cost = 1001
    for i in range(n):
        if time[i] <= t and c[i] < min_cost:
            min_cost = c[i]

    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 10

def solve(N, T, c, t):
    min_cost = 1001
    for i in range(N):
        if t[i] <= T and c[i] < min_cost:
            min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)
