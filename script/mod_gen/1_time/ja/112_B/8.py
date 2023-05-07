def main():
    N,T = map(int, input().split())
    c = []
    t = []
    for i in range(N):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        t.append(t_i)
    ans = 1000000
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    if ans == 1000000:
        print('TLE')
    else:
        print(ans)

if __name__ == '__main__':
    main()