def main():
    # 读取数据
    num = int(input())
    data = []
    for i in range(num):
        data.append(input().split())
    # 数据处理
    data.sort(key=lambda x: (x[0], -int(x[1])))
    # 输出结果
    for i in range(num):
        print(data[i][0], data[i][1])
