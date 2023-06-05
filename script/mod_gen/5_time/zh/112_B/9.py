def main():
    n,t = map(int,input().split())
    c = []
    T = []
    for i in range(n):
        c_i,t_i = map(int,input().split())
        c.append(c_i)
        T.append(t_i)
    c_min = 1000
    for i in range(n):
        if T[i] <= t:
            if c[i] < c_min:
                c_min = c[i]
    if c_min == 1000:
        print("TLE")
    else:
        print(c_min)

if __name__ == '__main__':
    main()