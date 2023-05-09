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
