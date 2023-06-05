def get_max_profit(N, Vs, Cs):
    max_profit = 0
    for i in range(1 << N):
        profit = 0
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                profit += Vs[j]
                cost += Cs[j]
        if profit > cost and profit - cost > max_profit:
            max_profit = profit - cost
    return max_profit

if __name__ == '__main__':
    get_max_profit()