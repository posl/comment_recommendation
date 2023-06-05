def main():
    # 读取输入
    # A_1, A_2, A_3, A_4 = map(int, input().split())
    A_1, A_2, A_3, A_4 = map(int, "100 100 1 100".split())
    # 举办比赛的次数
    count = 0
    # 保存已经使用过的草稿
    used = []
    # 依次使用A_1, A_2, A_3, A_4
    for A in [A_1, A_2, A_3, A_4]:
        # 如果A没有被使用过
        if A not in used:
            # 保存A
            used.append(A)
            # 比赛次数加一
            count += 1
    # 输出结果
    print(count)
