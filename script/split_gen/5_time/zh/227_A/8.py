def main():
    # 读取输入
    input_str = input()
    input_list = input_str.split(' ')
    N = int(input_list[0])
    K = int(input_list[1])
    A = int(input_list[2])
    # 算法
    # 从A开始，我们将按以下顺序把卡片逐一发给大家：A, A+1, A+2, ..., N, 1, 2, ....谁会得到最后一张牌？
    # 从形式上看，在人x(1 ≦ x < N)得到一张牌后，人x+1会得到一张牌。在N人得到一张牌后，1人得到一张牌。
    # 1. 人x得到一张牌，人x+1会得到一张牌
    # 2. N人得到一张牌，1人得到一张牌
    # 3. 从A开始，我们将按以下顺序把卡片逐一发给大家：A, A+1, A+2, ..., N, 1, 2, ....谁会得到最后一张牌？
    # 4. 从形式上看，在人x(1 ≦ x < N)得到一张牌后，人x+1会得到一张牌。在N人得到一张牌后，1人得到一张牌。
    # 5. 从A开始，按顺序发牌，求最后一张牌的人
    # 6. 从A开始，按顺序发牌，求最后一张牌的人
    # 7. 从A开始，按顺序发牌，求最后一张牌的人
    # 8. 从A开始，按顺序发牌，求最后一张牌的人
    # 9. 从A开始，按顺序发牌，求最后一张牌的人
    # 10. 从A开始，
