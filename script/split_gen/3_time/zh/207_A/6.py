def main():
    # 读入数据
    a, b, c = map(int, input().split())
    # 处理数据
    max_num = max(a, b, c)
    # 输出结果
    print(max_num*2 + a + b + c - max_num*3)
