def main():
    n,t = map(int,input().split())
    c = []
    time = []
    for i in range(n):
        c_time = list(map(int,input().split()))
        c.append(c_time[0])
        time.append(c_time[1])
    min_cost = 1001
    for i in range(n):
        if time[i] <= t:
            if c[i] < min_cost:
                min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    main()