def main():
    n, t = map(int, input().split())
    c = []
    time = []
    for i in range(n):
        c_i, t_i = map(int, input().split())
        c.append(c_i)
        time.append(t_i)
    min_c = 1001
    for i in range(n):
        if time[i] <= t:
            if c[i] < min_c:
                min_c = c[i]
    if min_c == 1001:
        print("TLE")
    else:
        print(min_c)

if __name__ == '__main__':
    main()