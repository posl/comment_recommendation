def main():
    # 读取输入
    n, k, a = map(int, input().split())
    # 模拟发卡
    cards = [i for i in range(1, k + 1)]
    for i in range(k):
        # 人数循环
        if i % n + 1 == a:
            # 该人拿到最后一张牌
            print(i % n + 1)
            break
        else:
            # 该人拿不到最后一张牌
            cards[i % n] = 0
