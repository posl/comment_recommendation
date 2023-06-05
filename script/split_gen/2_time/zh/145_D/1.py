def main():
    # 读入数据
    with open('problems145_c.txt', 'r') as f:
        n = int(f.readline())
        xy_list = []
        for i in range(n):
            xy_list.append(f.readline().split())
    # 计算距离
    distance_list = []
    for i in range(n):
        for j in range(i+1, n):
            distance = ((int(xy_list[i][0]) - int(xy_list[j][0])) ** 2 + (int(xy_list[i][1]) - int(xy_list[j][1])) ** 2) ** 0.5
            distance_list.append(distance)
    # 计算平均距离
    print(sum(distance_list) / len(distance_list))
