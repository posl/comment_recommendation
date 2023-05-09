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
