def main():
    # 读取输入
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    # 计算输出
    mountains.sort(key = lambda x: int(x[1]), reverse = True)
    print(mountains[1][0])
