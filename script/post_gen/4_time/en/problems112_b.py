Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c_i, t_i = map(int, input().split())
        if t_i <= t:
            c.append(c_i)
    if len(c) == 0:
        print('TLE')
    else:
        print(min(c))

=======
Suggestion 2

def solve():
    N, T = map(int, input().split())
    ans = T
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    if ans == T:
        print('TLE')
    else:
        print(ans)

=======
Suggestion 3

def main():
    n, t = map(int, input().split())
    c = []
    for _ in range(n):
        c_i, t_i = map(int, input().split())
        if t_i <= t:
            c.append(c_i)
    if len(c) == 0:
        print("TLE")
    else:
        print(min(c))

=======
Suggestion 4

def main():
    N,T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    min_cost = T
    for i in range(N):
        if t[i] <= T:
            min_cost = min(min_cost, c[i])
    if min_cost == T:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    routes = []
    for i in range(N):
        c, t = map(int, input().split())
        routes.append((c,t))
    routes.sort(key=lambda x: x[0])
    for c, t in routes:
        if t <= T:
            print(c)
            return
    print('TLE')

=======
Suggestion 6

def get_input():
    n, t = map(int, input().split())
    routes = []
    for i in range(n):
        c, t = map(int, input().split())
        routes.append((c, t))
    return t, routes

=======
Suggestion 7

def get_input():
    n,t = map(int,input().split())
    routes = []
    for i in range(n):
        c_i,t_i = map(int,input().split())
        routes.append((c_i,t_i))
    return n,t,routes

=======
Suggestion 8

def main():
    n, t = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(n)]
    ct.sort(key=lambda x: x[0])
    for c, t_ in ct:
        if t_ <= t:
            print(c)
            exit()
    print("TLE")

=======
Suggestion 9

def main():
    N, T = map(int, input().split())
    routes = [list(map(int, input().split())) for _ in range(N)]
    routes = sorted(routes, key=lambda x: x[0])
    for cost, time in routes:
        if time <= T:
            print(cost)
            exit()
    print('TLE')

=======
Suggestion 10

def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    cost = 1001
    for i in c:
        if i[1] <= t:
            if cost > i[0]:
                cost = i[0]
    if cost == 1001:
        print("TLE")
    else:
        print(cost)
