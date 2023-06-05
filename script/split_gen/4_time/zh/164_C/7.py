def main():
    # 读入
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # 处理
    s = set(s)
    # 输出
    print(len(s))
