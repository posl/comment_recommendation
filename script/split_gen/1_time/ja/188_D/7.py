def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    #各日にちにおける利用するサービスの個数
    use = [0]*(AB[-1][1]+1)
    for i in range(N):
        use[AB[i][0]] += 1
        use[AB[i][1]+1] -= 1
    #print(use)
    #各日にちにおける利用するサービスの個数の累積和
    for i in range(1, AB[-1][1]+1):
        use[i] += use[i-1]
    #print(use)
    #各日にちにおける利用するサービスの個数の累積和の最小値
    for i in range(1, AB[-1][1]+1):
        use[i] = min(use[i], use[i-1])
    #print(use)
    #各日にちにおけるサービスを利用するために支払う金額
    cost = [0]*(AB[-1][1]+1)
    for i in range(N):
        cost[AB[i][0]] += AB[i][2]
        cost[AB[i][1]+1] -= AB[i][2]
    #print(cost)
    #各日にちにおけるサービスを利用するために支払う金額の累積和
    for i in range(1, AB[-1][1]+1):
        cost[i] += cost[i-1]
    #print(cost)
    #各日にちにおけるサービスを利用するために支払う金額の累積和の最小値
    for i in range(1, AB[-1][1]+1):
        cost[i] = min(cost[i], cost[i-1])
    #print(cost)
    #各日にちにおけるサービスを利用
