def main():
    n,t = map(int,input().split())
    c = []
    time = []
    for i in range(n):
        c_i,t_i = map(int,input().split())
        c.append(c_i)
        time.append(t_i)
    cost = []
    for i in range(n):
        if time[i] <= t:
            cost.append(c[i])
    if len(cost) == 0:
        print('TLE')
    else:
        print(min(cost))
