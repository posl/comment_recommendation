def main():
    # 读入数据
    A, B, C, D, E, F, X = map(int, input().split())
    # 处理数据
    # 高桥走的距离
    takahashi = 0
    # 青木走的距离
    aoki = 0
    # 高桥的状态，True表示正在走，False表示正在休息
    takahashi_state = True
    # 青木的状态，True表示正在走，False表示正在休息
    aoki_state = True
    # 运动的时间
    time = 0
    # 开始慢跑
    while time < X:
        # 高桥走
        if takahashi_state:
            takahashi += B
            # 高桥走了A秒，休息C秒
            if takahashi >= A:
                takahashi_state = False
                takahashi = 0
        # 高桥休息
        else:
            takahashi += 1
            # 高桥休息了C秒，走A秒
            if takahashi >= C:
                takahashi_state = True
                takahashi = 0
        # 青木走
        if aoki_state:
            aoki += D
            # 青木走了E秒，休息F秒
            if aoki >= E:
                aoki_state = False
                aoki = 0
        # 青木休息
        else:
            aoki += 1
            # 青木休息了F秒，走E秒
            if aoki >= F:
                aoki_state = True
                aoki = 0
        # 时间增加
        time += 1
    # 判断谁走在前面
    if takahashi > aoki:
        print('高桥')
    elif takahashi < aoki:
        print('青木')
    else:
        print('画')
