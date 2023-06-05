def main():
    # 读入数据
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    # 从最高楼层开始，逐层向下检查
    # 当前楼层
    cur_floor = 10**9
    # 梯子编号
    cur_ladder = 0
    # 逐层向下检查
    while True:
        # 如果当前楼层是1层，则停止检查
        if cur_floor == 1:
            break
        # 逐个检查梯子
        for i in range(n):
            # 如果当前楼层在梯子的上端，则移动到下端
            if cur_floor == ab[i][1]:
                cur_floor = ab[i][0]
                cur_ladder = i + 1
                break
            # 如果当前楼层在梯子的下端，则移动到上端
            elif cur_floor == ab[i][0]:
                cur_floor = ab[i][1]
                cur_ladder = i + 1
                break
    # 输出结果
    print(cur_ladder)

if __name__ == '__main__':
    main()