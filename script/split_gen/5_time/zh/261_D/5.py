def get_max_money(N, M, X, C, Y):
    max_money = 0
    for i in range(2**N):
        money = 0
        count = 0
        for j in range(N):
            if i & 1 << j:
                count += 1
                money += X[j]
        for k in range(M):
            if count == C[k]:
                money += Y[k]
        if money > max_money:
            max_money = money
    return max_money
