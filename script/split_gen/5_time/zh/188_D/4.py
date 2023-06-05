def main():
    N, C = map(int, input().split())
    service = []
    for i in range(N):
        service.append(list(map(int, input().split())))
    service.sort()
    #print(service)
    #计算每天的费用
    daily_cost = [0] * (service[-1][1] + 1)
    for i in range(N):
        daily_cost[service[i][0] - 1] += service[i][2]
        daily_cost[service[i][1]] -= service[i][2]
    #print(daily_cost)
    #计算每天的费用累计和
    daily_cost_sum = [0] * (service[-1][1] + 1)
    daily_cost_sum[0] = daily_cost[0]
    for i in range(1, service[-1][1] + 1):
        daily_cost_sum[i] = daily_cost_sum[i - 1] + daily_cost[i]
    #print(daily_cost_sum)
    #计算每天的费用累计和的最小值
    daily_cost_sum_min = [0] * (service[-1][1] + 1)
    daily_cost_sum_min[0] = daily_cost_sum[0]
    for i in range(1, service[-1][1] + 1):
        daily_cost_sum_min[i] = min(daily_cost_sum_min[i - 1], daily_cost_sum[i])
    #print(daily_cost_sum_min)
    #计算最小总金额
    total_cost = 0
    for i in range(service[-1][1] + 1):
        if daily_cost_sum_min[i] * C < daily_cost_sum[i]:
            total_cost += daily_cost_sum_min[i] * C
        else:
            total_cost += daily_cost_sum[i]
    print(total_cost)
