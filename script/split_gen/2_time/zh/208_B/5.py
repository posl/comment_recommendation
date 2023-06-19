def coin_problem(p):
    coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    count = 0
    for i in range(8, -1, -1):
        count += p // coin[i]
        p = p % coin[i]
    return count
