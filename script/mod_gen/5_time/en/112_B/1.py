def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    c = [c_i for _, c_i in sorted(zip(t, c))]
    t = sorted(t)
    for i in range(N):
        if t[i] <= T:
            print(c[i])
            break
        if i == N - 1:
            print("TLE")

if __name__ == '__main__':
    main()