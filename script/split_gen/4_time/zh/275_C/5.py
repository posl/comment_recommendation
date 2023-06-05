def main():
    # 读取输入
    s_list = []
    for i in range(9):
        s_list.append(input())
    # print(s_list)
    # 遍历所有的格子
    count = 0
    for i in range(9):
        for j in range(9):
            # 顶点有棋子
            if s_list[i][j] == "#":
                # 向右下角遍历
                for k in range(1, 9 - max(i, j)):
                    if s_list[i + k][j + k] == "#":
                        # 向左下角遍历
                        for l in range(1, min(j, 9 - i)):
                            if s_list[i + l][j - l] == "#":
                                # 向左上角遍历
                                for m in range(1, min(i, j)):
                                    if s_list[i - m][j - m] == "#":
                                        # 向右上角遍历
                                        for n in range(1, min(9 - i, j)):
                                            if s_list[i + n][j - n] == "#":
                                                count += 1
    print(count)
