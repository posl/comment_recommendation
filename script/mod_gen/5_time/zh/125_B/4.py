def get_max_profit(N, V, C):
    max_profit = 0
    for i in range(2**N):
        profit = 0
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                profit += V[j]
                cost += C[j]
        if profit - cost > max_profit:
            max_profit = profit - cost
    return max_profit

if __name__ == '__main__':
    get_max_profit()