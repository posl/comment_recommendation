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
