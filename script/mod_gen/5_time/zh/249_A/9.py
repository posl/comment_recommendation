def run():
    # 读取输入
    A, B, C, D, E, F, X = map(int, input().split())
    # 高桥和青木的位置
    t, h = 0, 0
    # 循环
    while True:
        # 高桥行走
        t += A
        # 判断
        if t >= X:
            print('高桥')
            break
        # 青木行走
        h += D
        # 判断
        if h >= X:
            print('青木')
            break
        # 高桥休息
        t += C
        # 判断
        if t >= X:
            print('高桥')
            break
        # 青木休息
        h += F
        # 判断
        if h >= X:
            print('青木')
            break

if __name__ == '__main__':
    run()