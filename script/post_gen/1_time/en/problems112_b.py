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
    min_c = 1001
    for i in range(N):
        if t[i] <= T and c[i] < min_c:
            min_c = c[i]
    if min_c == 1001:
        print("TLE")
    else:
        print(min_c)

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    routes = []
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T:
            routes.append(c)
    if len(routes) == 0:
        print("TLE")
    else:
        print(min(routes))

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
    min_c = T
    for i in range(N):
        if t[i] <= T:
            min_c = min(min_c, c[i])
    if min_c == T:
        print("TLE")
    else:
        print(min_c)

=======
Suggestion 4

def main():
    n, t = map(int, input().split())
    routes = []
    for i in range(n):
        route = list(map(int, input().split()))
        if route[1] <= t:
            routes.append(route[0])
    if len(routes) == 0:
        print('TLE')
    else:
        print(min(routes))

=======
Suggestion 5

def main():
    n, t = map(int, input().split())
    cost = 1001
    for i in range(n):
        c, ti = map(int, input().split())
        if ti <= t:
            cost = min(cost, c)
    if cost == 1001:
        print('TLE')
    else:
        print(cost)

=======
Suggestion 6

def get_min_cost(N, T, routes):
    min_cost = T
    for route in routes:
        if route[1] <= T and route[0] < min_cost:
            min_cost = route[0]
    if min_cost == T:
        return "TLE"
    else:
        return min_cost

=======
Suggestion 7

def get_input():
    n, t = map(int, input().split())
    routes = []
    for i in range(n):
        c, t_i = map(int, input().split())
        routes.append((c, t_i))
    return n, t, routes

=======
Suggestion 8

def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    c.sort(key=lambda x: x[0])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            break
    else:
        print("TLE")

=======
Suggestion 9

def get_input():
    n, t = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(n)]
    return n, t, ct

=======
Suggestion 10

def main():
    n,t = map(int,input().split())
    c = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    c.sort(key=lambda x:x[0])
    c.sort(key=lambda x:x[1])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            break
        if i == n-1:
            print("TLE")
            break
