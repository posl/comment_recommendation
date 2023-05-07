def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    cost = 1001
    for i in range(N):
        if t[i] <= T and c[i] < cost:
            cost = c[i]
    if cost == 1001:
        print("TLE")
    else:
        print(cost)
