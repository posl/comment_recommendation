def main():
    n, t = map(int, input().split())
    c = []
    time = []
    for i in range(n):
        c1, time1 = map(int, input().split())
        c.append(c1)
        time.append(time1)
    min_cost = 1001
    for i in range(n):
        if time[i] <= t:
            if min_cost > c[i]:
                min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)
