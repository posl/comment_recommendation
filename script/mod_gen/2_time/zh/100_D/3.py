def get_max_value(N, M, cakes):
    # 1. 选出最大的M个蛋糕
    cakes.sort(key=lambda x: abs(x[0]) + abs(x[1]) + abs(x[2]), reverse=True)
    # 2. 计算最大的M个蛋糕的总美丽度、美味度和受欢迎度
    total_beauty = sum([cake[0] for cake in cakes[:M]])
    total_delicious = sum([cake[1] for cake in cakes[:M]])
    total_popularity = sum([cake[2] for cake in cakes[:M]])
    # 3. 如果有负值，则把负号去掉
    if total_beauty < 0:
        total_beauty = -total_beauty
    if total_delicious < 0:
        total_delicious = -total_delicious
    if total_popularity < 0:
        total_popularity = -total_popularity
    # 4. 返回最大的M个蛋糕的总美丽度、美味度和受欢迎度
    return total_beauty + total_delicious + total_popularity

if __name__ == '__main__':
    get_max_value()