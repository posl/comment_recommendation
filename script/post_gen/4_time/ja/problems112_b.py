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
            min_cost = min(min_cost, c[i])

    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    C = []
    T = []
    for i in range(N):
        c, t = map(int, input().split())
        C.append(c)
        T.append(t)
    ans = 1000
    for i in range(N):
        if T[i] <= T:
            ans = min(ans, C[i])
    if ans == 1000:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 3

def solve():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
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
    N, T = map(int, input().split())
    lst = []
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T:
            lst.append(c)
    if len(lst) == 0:
        print('TLE')
    else:
        print(min(lst))

=======
Suggestion 5

def main():
    n, t = map(int, input().split())
    c = []
    time = []
    for i in range(n):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        time.append(t_i)
    min_c = 1001
    for i in range(n):
        if time[i] <= t:
            if c[i] < min_c:
                min_c = c[i]
    if min_c == 1001:
        print("TLE")
    else:
        print(min_c)

=======
Suggestion 6

def main():
    n,t = map(int, input().split())
    c = [0]*n
    t = [0]*n
    for i in range(n):
        c[i],t[i] = map(int, input().split())
    min_c = 1001
    for i in range(n):
        if t[i] <= t and c[i] < min_c:
            min_c = c[i]
    if min_c == 1001:
        print("TLE")
    else:
        print(min_c)

=======
Suggestion 7

def main():
    n, t = map(int, input().split())
    ans = 1000
    for _ in range(n):
        c, ti = map(int, input().split())
        if ti <= t and ans > c:
            ans = c
    if ans == 1000:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 8

def main():
    N,T = map(int,input().split())
    c = []
    t = []
    for i in range(N):
        a,b = map(int,input().split())
        c.append(a)
        t.append(b)
    cost = 1001
    for i in range(N):
        if t[i] <= T:
            if c[i] < cost:
                cost = c[i]
    if cost == 1001:
        print("TLE")
    else:
        print(cost)

=======
Suggestion 9

def main():
    n,t = map(int,input().split())
    routes = []
    for _ in range(n):
        c_i,t_i = map(int,input().split())
        if t_i <= t:
            routes.append([c_i,t_i])
    if len(routes) == 0:
        print("TLE")
    else:
        routes.sort(key=lambda x:x[0])
        print(routes[0][0])

=======
Suggestion 10

def main():
    # 整数の入力
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))

    #print(n)
    #print(t)
    #print(c)

    min_cost = 1000
    for i in range(n):
        if c[i][1] <= t:
            if c[i][0] < min_cost:
                min_cost = c[i][0]

    if min_cost == 1000:
        print("TLE")
    else:
        print(min_cost)
