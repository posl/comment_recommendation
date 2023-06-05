def coin_combination():
    # 1. 输入
    p = int(input())
    # 2. 初始化
    coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coin.reverse()
    # 3. 处理
    count = 0
    for i in coin:
        while p >= i:
            p -= i
            count += 1
    # 4. 输出
    print(count)
coin_combination()
