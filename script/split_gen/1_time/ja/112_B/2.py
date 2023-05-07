def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    cost = 1000
    for i in range(N):
        if t[i] <= T:
            if c[i] < cost:
                cost = c[i]
    if cost == 1000:
        print('TLE')
    else:
        print(cost)
