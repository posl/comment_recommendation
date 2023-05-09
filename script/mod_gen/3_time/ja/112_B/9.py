def main():
    # データ入力
    n, t = map(int, input().split())
    # データ入力
    cost = []
    time = []
    for i in range(n):
        c, ti = map(int, input().split())
        cost.append(c)
        time.append(ti)
    # 初期化
    min_cost = 1000
    # 計算
    for i in range(n):
        if time[i] <= t:
            if cost[i] < min_cost:
                min_cost = cost[i]
    # 出力
    if min_cost == 1000:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    main()