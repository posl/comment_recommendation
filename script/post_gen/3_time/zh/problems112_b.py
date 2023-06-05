Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    c.sort(key=lambda x: x[1])
    for i in range(n):
        if c[i][1] > t:
            c.pop(i)
            break
    if len(c) == 0:
        print("TLE")
    else:
        print(min(c, key=lambda x: x[0])[0])

=======
Suggestion 2

def get_input():
    N, T = map(int, input().split())
    c_t = []
    for i in range(N):
        c_t.append(list(map(int, input().split())))
    return N, T, c_t

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    routes = []
    for i in range(N):
        c, t = map(int, input().split())
        routes.append((c, t))
    routes.sort(key=lambda x: x[1])
    # print(routes)
    # if routes[0][1] > T:
    #     print("TLE")
    #     return
    dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]
    # print(dp)
    for i in range(1, N + 1):
        for j in range(1, T + 1):
            if routes[i - 1][1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - routes[i - 1][1]] + routes[i - 1][0])
            else:
                dp[i][j] = dp[i - 1][j]
    # print(dp)
    if dp[N][T] == 0:
        print("TLE")
    else:
        print(dp[N][T])

=======
Suggestion 4

def searchBestRoute(N, T, c, t):
    if N <= 0:
        return 0
    if T <= 0:
        return 0
    if T < min(t):
        return 0
    if T == min(t):
        return min(c)
    if N == 1:
        return c[0]
    if N == 2:
        if T >= t[0] and T >= t[1]:
            return min(c)
        elif T >= t[0] and T < t[1]:
            return c[0]
        elif T >= t[1] and T < t[0]:
            return c[1]
        else:
            return 0
    if N > 2:
        if T >= t[0]:
            return min(c[0] + searchBestRoute(N - 1, T - t[0], c[1:], t[1:]),
                       searchBestRoute(N - 1, T, c[1:], t[1:]))
        else:
            return searchBestRoute(N - 1, T, c[1:], t[1:])

=======
Suggestion 5

def calc_cost(cost, time):
    if time <= T:
        return cost
    else:
        return 1001

=======
Suggestion 6

def get_input():
    N, T = input().split()
    N = int(N)
    T = int(T)
    if N < 1 or N > 100 or T < 1 or T > 1000:
        return None
    c = []
    t = []
    for i in range(N):
        c_i, t_i = input().split()
        c_i = int(c_i)
        t_i = int(t_i)
        if c_i < 1 or c_i > 1000 or t_i < 1 or t_i > 1000:
            return None
        c.append(c_i)
        t.append(t_i)
    return N, T, c, t

=======
Suggestion 7

def main():
  n, t = map(int, input().split())
  data = [[int(x) for x in input().split()] for _ in range(n)]
  data.sort(key=lambda x: x[1])
  ans = 1000
  for i in range(n):
    if data[i][1] <= t:
      ans = min(ans, data[i][0])
  if ans == 1000:
    print("TLE")
  else:
    print(ans)

main()

=======
Suggestion 8

def solve():
    N, T = map(int, input().split())
    costs = []
    times = []
    for _ in range(N):
        c, t = map(int, input().split())
        costs.append(c)
        times.append(t)

    min_cost = 1001
    for i in range(N):
        if times[i] <= T:
            min_cost = min(min_cost, costs[i])

    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 9

def solve():
    N, T = map(int, input().split())
    ans = 1001
    for i in range(N):
        c, t = map(int, input().split())
        if t <= T and c < ans:
            ans = c
    if ans == 1001:
        print("TLE")
    else:
        print(ans)

solve()

=======
Suggestion 10

def solve(n, t, c, ti):
    res = t
    for i in range(n):
        if ti[i] <= t:
            res = min(res, c[i])
    if res == t:
        return "TLE"
    else:
        return res
