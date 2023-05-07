def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    min_c = 1001
    for i in range(N):
        if t[i] <= T and c[i] < min_c:
            min_c = c[i]
    if min_c == 1001:
        print("TLE")
    else:
        print(min_c)

if __name__ == '__main__':
    main()