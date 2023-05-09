def main():
    N, T = map(int, input().split())
    #print(N, T)
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    #print(c, t)
    ans = 10000
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    if ans == 10000:
        print('TLE')
    else:
        print(ans)
