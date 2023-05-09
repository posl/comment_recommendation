def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for _ in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    #print(c)
    #print(t)
    min_cost = 1000
    for i in range(N):
        if t[i] <= T:
            if c[i] < min_cost:
                min_cost = c[i]
    if min_cost == 1000:
        print("TLE")
    else:
        print(min_cost)
