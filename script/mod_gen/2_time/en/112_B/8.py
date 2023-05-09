def main():
    #入力
    N, T = map(int, input().split())
    #各ルートのコストと時間をリストに格納
    cost = []
    time = []
    for i in range(N):
        c, t = map(int, input().split())
        cost.append(c)
        time.append(t)
    #ルートの時間がT以下のものの中でコストが最小のものを探す
    ans = 1000
    for i in range(N):
        if time[i] <= T:
            if cost[i] < ans:
                ans = cost[i]
    #出力
    if ans == 1000:
        print("TLE")
    else:
        print(ans)

if __name__ == '__main__':
    main()