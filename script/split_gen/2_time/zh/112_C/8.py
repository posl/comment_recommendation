def main():
    # 读取输入
    N = int(input())
    xyz = []
    for i in range(N):
        xyz.append(list(map(int, input().split())))
    # print(N)
    # print(xyz)
    # 遍历所有可能的C_X,C_Y,H
    for C_X in range(101):
        for C_Y in range(101):
            for H in range(1, 101):
                # print(C_X, C_Y, H)
                # 计算所有坐标的高度，保存在列表中
                H_list = []
                for x, y, h in xyz:
                    H_list.append(max(H - abs(x - C_X) - abs(y - C_Y), 0))
                # print(H_list)
                # 遍历所有坐标的高度，判断是否与输入的高度相等
                for i in range(N):
                    if H_list[i] != xyz[i][2]:
                        break
                else:
                    print(C_X, C_Y, H)
                    return
