def main():
    # 读入数据
    x = list(map(int, input().split()))
    # 计算结果
    for i in range(5):
        if x[i] == 0:
            print(i + 1)
            break
