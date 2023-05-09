def main():
    N,T = map(int,input().split())
    t = []
    c = []
    for i in range(N):
        c_i,t_i = map(int,input().split())
        t.append(t_i)
        c.append(c_i)
    min_c = 1001
    for i in range(N):
        if t[i] <= T:
            if min_c > c[i]:
                min_c = c[i]
    if min_c == 1001:
        print("TLE")
    else:
        print(min_c)
