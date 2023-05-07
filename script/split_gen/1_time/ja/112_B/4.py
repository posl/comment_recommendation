def main():
    N, T = map(int, input().split())
    cost = []
    time = []
    for i in range(N):
        c, t = map(int, input().split())
        cost.append(c)
        time.append(t)
    ans = 1001
    for i in range(N):
        if time[i] <= T:
            ans = min(ans, cost[i])
    if ans == 1001:
        print("TLE")
    else:
        print(ans)
