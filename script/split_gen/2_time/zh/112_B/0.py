def main():
    n,t = map(int,input().split())
    c = []
    time = []
    for i in range(n):
        ci,ti = map(int,input().split())
        c.append(ci)
        time.append(ti)
    min_cost = t
    for i in range(n):
        if time[i] <= t and c[i] < min_cost:
            min_cost = c[i]
    if min_cost == t:
        print("TLE")
    else:
        print(min_cost)
