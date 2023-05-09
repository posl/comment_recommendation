def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        ci, ti = map(int, input().split())
        c.append(ci)
        t.append(ti)
    c_min = 1000
    for i in range(N):
        if t[i] <= T:
            if c[i] < c_min:
                c_min = c[i]
    if c_min == 1000:
        print("TLE")
    else:
        print(c_min)

if __name__ == '__main__':
    main()