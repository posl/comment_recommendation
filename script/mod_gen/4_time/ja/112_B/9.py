def main():
    # 整数の入力
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    #print(n)
    #print(t)
    #print(c)
    min_cost = 1000
    for i in range(n):
        if c[i][1] <= t:
            if c[i][0] < min_cost:
                min_cost = c[i][0]
    if min_cost == 1000:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    main()