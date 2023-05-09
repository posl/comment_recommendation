def main():
    N,T = map(int,input().split())
    c = []
    t = []
    for i in range(N):
        a,b = map(int,input().split())
        c.append(a)
        t.append(b)
    cost = 1001
    for i in range(N):
        if t[i] <= T:
            if c[i] < cost:
                cost = c[i]
    if cost == 1001:
        print("TLE")
    else:
        print(cost)
