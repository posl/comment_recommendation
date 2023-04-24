Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    c = [0] * N
    t = [0] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())
    min_c = 1000
    for i in range(N):
        if t[i] <= T and c[i] < min_c:
            min_c = c[i]
    if min_c == 1000:
        print("TLE")
    else:
        print(min_c)

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    c = [0] * N
    t = [0] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())

    ans = 1001
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])

    if ans == 1001:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 3

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
        print('TLE')
    else:
        print(min_cost)

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    C = []
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            C.append(c)
    if C:
        print(min(C))
    else:
        print('TLE')

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    min_cost = 1001
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T and c < min_cost:
            min_cost = c
    print(min_cost if min_cost < 1001 else "TLE")

main()

=======
Suggestion 6

def main():
    N, T = map(int, input().split())
    ans = 10**9+1
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    if ans == 10**9+1:
        print("TLE")
    else:
        print(ans)

=======
Suggestion 7

def main():
    N, T = map(int, input().split())
    routes = [tuple(map(int, input().split())) for _ in range(N)]
    routes.sort(key=lambda x: x[0])
    min_cost = float('inf')
    for i in range(N):
        if routes[i][1] <= T:
            min_cost = min(min_cost, routes[i][0])
    if min_cost == float('inf'):
        print('TLE')
    else:
        print(min_cost)

=======
Suggestion 8

def main():
    # Read data
    N, T = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(N)]

    # Solve
    ans = 1001
    for i in range(N):
        if ct[i][1] <= T:
            ans = min(ans, ct[i][0])

    if ans == 1001:
        print('TLE')
    else:
        print(ans)

=======
Suggestion 9

def main():
    #入力
    N, T = map(int, input().split())
    #各ルートのコストと時間をリストに格納
    cost = []
    time = []
    for i in range(N):
        c, t = map(int, input().split())
        cost.append(c)
        time.append(t)
    #ルートの時間がT以下のものの中でコストが最小のものを探す
    ans = 1000
    for i in range(N):
        if time[i] <= T:
            if cost[i] < ans:
                ans = cost[i]
    #出力
    if ans == 1000:
        print("TLE")
    else:
        print(ans)
