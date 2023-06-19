def main():
    # 读取输入
    a1, a2, a3, a4 = map(int, input().split())
    # 用来记录草稿的使用次数
    count = 0
    # 用来记录当前草稿是否已经使用过
    flag = [False, False, False, False]
    # 对草稿进行排序
    draft = sorted([a1, a2, a3, a4])
    # 从大到小遍历草稿
    for i in range(3, -1, -1):
        # 如果当前草稿未使用过
        if flag[i] == False:
            # 将当前草稿标记为已使用
            flag[i] = True
            # 将当前草稿加入到总数中
            count += 1
            # 遍历剩余的草稿
            for j in range(i - 1, -1, -1):
                # 如果当前草稿未使用过
                if flag[j] == False:
                    # 如果当前草稿与已使用的草稿之和等于100
                    if draft[i] + draft[j] == 100:
                        # 将当前草稿标记为已使用
                        flag[j] = True
                        # 跳出循环
                        break
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()