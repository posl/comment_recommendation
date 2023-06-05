def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # 每张牌被吃掉的步数
    step = [-1] * N
    # 每张牌的位置
    position = [-1] * N
    for i in range(N):
        position[P[i]-1] = i
    # 当前桌面上的牌
    table = []
    for i in range(N):
        # 抽出的牌
        card = P[i]
        # 抽出的牌在桌面上的位置
        card_pos = position[card-1]
        # 抽出的牌放在桌面上
        table.append(card)
        # 抽出的牌在桌面上的位置
        table_pos = len(table) - 1
        # 如果桌面上有K张牌，吃掉
        if len(table) == K:
            for j in range(K):
                table.pop(0)
        # 抽出的牌的位置
        step[card-1] = card_pos - table_pos
    for i in range(N):
        print(step[i])

if __name__ == '__main__':
    main()