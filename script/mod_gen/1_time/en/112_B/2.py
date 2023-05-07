def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for _ in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    min_c = T
    for i in range(N):
        if t[i] <= T:
            min_c = min(min_c, c[i])
    if min_c == T:
        print("TLE")
    else:
        print(min_c)

if __name__ == '__main__':
    main()