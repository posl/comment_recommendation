def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    #print(N, K)
    #print(x)
    # 从0开始的时间
    time = 0
    # 从0开始向左移动的时间
    time_left = 0
    # 从0开始向右移动的时间
    time_right = 0
    # 将x列表中的正负数分开
    x_left = []
    x_right = []
    for i in x:
        if i < 0:
            x_left.append(i)
        elif i > 0:
            x_right.append(i)
        else:
            pass
    #print(x_left)
    #print(x_right)
    #print(len(x_left))
    #print(len(x_right))
    # 从0开始向左移动的时间
    if len(x_left) > 0:
        time_left = abs(x_left[0])
    # 从0开始向右移动的时间
    if len(x_right) > 0:
        time_right = x_right[-1]
    #print(time_left)
    #print(time_right)
    # 从0开始向左移动的时间和向右移动的时间，取大的值
    time = max(time_left, time_right)
    #print(time)
    # 从0开始的时间，加上从0开始向左移动的时间和向右移动的时间
    time = time + (time_right - time_left)
    #print(time)
    # 从0开始的时间，加上从0开始向左移动的时间和向右移动的时间，再加上点燃蜡烛的时间
    time = time + (x_right[-1] - x_left[0])
    #print(time)
    # 从0开始的时间，加上从0开始向左移动的时间和向右移动的时间，再加上点燃蜡烛的时间，再减去点燃K支蜡烛的时间
    time = time - x_right[-K]
    #print(time)
    # 从0开始的时间，加上从0

if __name__ == '__main__':
    main()