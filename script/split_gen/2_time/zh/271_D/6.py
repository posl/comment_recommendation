def check_sum(n, s, cards):
    if n < 1:
        return False
    if s < 1:
        return False
    if len(cards) != n:
        return False
    # 筛选出所有的可能性
    # 1. 每张牌都正面朝上
    # 2. 每张牌都背面朝上
    # 3. 每张牌都正面朝上或者背面朝上
    # 1. 每张牌都正面朝上
    sum = 0
    for i in range(n):
        sum += cards[i][0]
    if sum == s:
        return True
    # 2. 每张牌都背面朝上
    sum = 0
    for i in range(n):
        sum += cards[i][1]
    if sum == s:
        return True
    # 3. 每张牌都正面朝上或者背面朝上
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                if k == i:
                    sum += cards[k][0]
                elif k == j:
                    sum += cards[k][1]
                else:
                    if cards[k][0] > cards[k][1]:
                        sum += cards[k][0]
                    else:
                        sum += cards[k][1]
            if sum == s:
                return True
    return False
