def main():
    # 读取输入
    x = list(map(int, input().split()))
    # 处理
    for i in range(5):
        if x[i] == 0:
            print(i + 1)
            break
