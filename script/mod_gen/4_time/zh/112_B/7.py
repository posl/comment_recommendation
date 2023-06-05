def main():
    n,t = map(int,input().split())
    c = []
    tt = []
    for i in range(n):
        a,b = map(int,input().split())
        c.append(a)
        tt.append(b)
    min_cost = 1001
    for i in range(n):
        if tt[i] <= t and c[i] < min_cost:
            min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    main()