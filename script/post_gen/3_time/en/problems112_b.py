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

main()

My code is here.

I have a question. I have a list of lists. I want to find the index of the smallest value in each list. For example, if I have a list of lists like this:

[[1, 2, 3], [2, 1, 3], [1, 3, 2]]

I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?

I have a list of lists. I want to find the index of the smallest value in each list. For example, if I have a list of lists like this:

[[1, 2, 3], [2, 1, 3], [1, 3, 2]]

I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?

I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?

I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?

I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?

I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?

I want to find the index of the smallest value in each list. In this case, the answer is 0, 1, 0. How can I do that?

I want to find the index

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        ci, ti = map(int, input().split())
        c.append(ci)
        t.append(ti)
    c_min = 1000
    for i in range(N):
        if t[i] <= T:
            if c[i] < c_min:
                c_min = c[i]
    if c_min == 1000:
        print("TLE")
    else:
        print(c_min)

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    c = [0]*N
    t = [0]*N
    for i in range(N):
        c[i], t[i] = map(int, input().split())
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
Suggestion 5

def main():
    N, T = map(int, input().split())
    ans = 1000
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    if ans == 1000:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 6

def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for _ in range(N):
        _c, _t = map(int, input().split())
        c.append(_c)
        t.append(_t)
    ans = 1001
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    if ans == 1001:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 7

def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_, t_ = map(int, input().split())
        c.append(c_)
        t.append(t_)
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
Suggestion 8

def solve():
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

solve()

I solved this problem by using a greedy algorithm. If the time is less than or equal to the time limit, then check if the cost is less than the minimum cost. If it is, update the minimum cost. If the minimum cost is not updated, then there is no route that takes not longer than time T. In this case, print TLE instead.

=======
Suggestion 9

def main():
    N,T = map(int,input().split())
    t = []
    c = []
    for i in range(N):
        c_i,t_i = map(int,input().split())
        t.append(t_i)
        c.append(c_i)
    min_c = 1001
    for i in range(N):
        if t[i] <= T:
            if min_c > c[i]:
                min_c = c[i]
    if min_c == 1001:
        print("TLE")
    else:
        print(min_c)

=======
Suggestion 10

def main():
    N, T = [int(x) for x in input().split()]
    routes = [tuple(int(x) for x in input().split()) for _ in range(N)]
    routes.sort(key = lambda x: x[1])
    min_cost = 1001
    for cost, time in routes:
        if time > T:
            break
        min_cost = min(min_cost, cost)
    print(min_cost if min_cost < 1001 else "TLE")
