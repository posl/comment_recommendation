def main():
    # 读取数据
    a, b = map(int, input().split())
    # 计算最少电源条数
    if b % a == 0:
        print(b//a)
    else:
        print(b//a+1)
