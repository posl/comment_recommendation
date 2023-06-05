def main():
    # 读入数据
    S = input()
    # print(S)
    # 初始化
    # 从左到右的方向
    left_to_right = True
    # 记录每个方格上的小孩数
    child_count = [1]*len(S)
    # print(child_count)
    # 按照方向进行移动
    for i in range(100):
        # print(i)
        # print(child_count)
        # print(left_to_right)
        # print(S)
        # print()
        # 移动
        if left_to_right:
            # 从左到右移动
            for j in range(len(S)-1):
                if S[j] == 'R' and S[j+1] == 'L':
                    child_count[j] += child_count[j+1]
                    child_count[j+1] = 0
            left_to_right = False
        else:
            # 从右到左移动
            for j in range(len(S)-1,0,-1):
                if S[j] == 'L' and S[j-1] == 'R':
                    child_count[j] += child_count[j-1]
                    child_count[j-1] = 0
            left_to_right = True
    # 输出
    print(' '.join(map(str, child_count)))

if __name__ == '__main__':
    main()