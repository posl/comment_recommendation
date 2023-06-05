def main():
    n, k = map(int, input().split())
    cards = list(map(int, input().split()))
    # print(n, k, cards)
    # 1. cards中每个元素的索引值就是牌的数字，值就是牌的位置
    # 2. 用一个列表记录每个牌的位置
    # 3. 用一个列表记录每个牌是否被吃掉
    # 4. 用一个列表记录每个牌被吃掉的步数
    cards_position = [0] * (n + 1)
    cards_eaten = [False] * (n + 1)
    cards_eaten_step = [0] * (n + 1)
    for i in range(1, n + 1):
        cards_position[cards[i - 1]] = i
    # print(cards_position)
    for i in range(1, n + 1):
        if cards_eaten[i]:
            continue
        # print(i)
        cards_eaten[i] = True
        cards_eaten_step[i] = 0
        cards_eaten_count = 1
        next_card = cards_position[i]
        # print(next_card)
        while next_card != i:
            if cards_eaten[next_card]:
                break
            cards_eaten[next_card] = True
            cards_eaten_count += 1
            cards_eaten_step[next_card] = cards_eaten_step[i] + cards_eaten_count
            next_card = cards_position[next_card]
    # print(cards_eaten_step)
    for i in range(1, n + 1):
        print(cards_eaten_step[i])
