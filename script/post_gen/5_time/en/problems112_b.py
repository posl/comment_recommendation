Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    c = [0] * N
    t = [0] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())

    cost = T + 1
    for i in range(N):
        if t[i] <= T and c[i] < cost:
            cost = c[i]

    if cost == T + 1:
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

    c = [c_i for _, c_i in sorted(zip(t, c))]
    t = sorted(t)

    for i in range(N):
        if t[i] <= T:
            print(c[i])
            break
        if i == N - 1:
            print("TLE")

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    min_cost = T + 1
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T and c < min_cost:
            min_cost = c
    if min_cost == T + 1:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 4

def main():
    n, t = map(int, input().split())
    min_cost = t
    for i in range(n):
        c, ti = map(int, input().split())
        if ti <= t and c < min_cost:
            min_cost = c
    if min_cost == t:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 5

def main():
    n, t = map(int, input().split())
    c = 1001
    for i in range(n):
        ci, ti = map(int, input().split())
        if ti <= t:
            c = min(c, ci)
    if c == 1001:
        print("TLE")
    else:
        print(c)

=======
Suggestion 6

def get_input():
    n, t = map(int, input().split())
    routes = []
    for i in range(n):
        route = list(map(int, input().split()))
        routes.append(route)
    return t, routes

=======
Suggestion 7

def main():
    n,t = map(int,input().split())
    c = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    c.sort(key=lambda x:x[1])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            break
    else:
        print('TLE')

=======
Suggestion 8

def find_route(routes, time):
    min_cost = time + 1
    for route in routes:
        if route[1] <= time:
            if route[0] < min_cost:
                min_cost = route[0]
    if min_cost > time:
        return 'TLE'
    else:
        return min_cost

=======
Suggestion 9

def get_data():
    n, t = list(map(int, input().split()))
    routes = []
    for i in range(n):
        c, t = list(map(int, input().split()))
        routes.append((c, t))
    return t, routes

=======
Suggestion 10

def main():
    from sys import stdin
    #n = int(input())
    #a, b = map(int, input().split())
    #s = input()
    #a = list(map(int, input().split()))
    n, t = map(int, stdin.readline().split())
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, input().split())) for _ in range(n)]
    #a = [stdin.readline().strip() for _ in range(n)]
    #a = stdin.readlines()
    #a = [int(s) for s in stdin.readlines()]
    #a = [stdin.readline().strip() for _ in range(n)]
    #a = [int(stdin.readline()) for _ in range(n)]
    #a = [list(map(int, stdin.readline().split())) for _ in range(n)]
    #a = [stdin.readline().strip() for _ in range(n)]
    #a = [list(map(int, stdin.readline().split())) for _ in range(n)]
    #a = [list(map(int, stdin.readline().split())) for _ in range(n)]
    #a = stdin.read().splitlines()
    #a = [int(s) for s in stdin.read().splitlines()]
    #a = [stdin.readline().strip() for _ in range(n)]
    #a = [int(stdin.readline()) for _ in range(n)]
    #a = [list(map(int, stdin.readline().split())) for _ in range(n)]
    #a = [stdin.readline().strip() for _ in range(n)]
    #a = [list(map(int, stdin.readline().split())) for _ in range(n)]
    #a = [list(map(int, stdin.readline().split())) for _ in range(n)]
    #a = stdin.read().splitlines()
    #a = [int(s) for s in stdin.read().splitlines()]
    #a = [stdin.readline().strip() for _ in range(n)]
    #a = [int(stdin.readline()) for _ in range(n)]
    #a = [list(map(int, stdin.readline().split())) for _ in range(n)]
    #a = [stdin.readline().strip() for _ in range(n)]
    a = [list(map(int, stdin.readline().split())) for _ in range(n)]
    #a = [list(map(int, stdin.readline().split())) for _ in
