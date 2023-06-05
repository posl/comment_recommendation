def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # 用列表保存天线坐标
    antenna = [a, b, c, d, e]
    # 用列表保存天线之间的距离
    distance = []
    # 计算天线之间的距离
    for i in range(len(antenna)):
        for j in range(i + 1, len(antenna)):
            distance.append(antenna[j] - antenna[i])
    # 如果存在天线之间的距离大于k，则输出 :(，否则输出 Yay!
    if max(distance) > k:
        print(':(')
    else:
        print('Yay!')
