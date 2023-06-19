def main():
    # 读取输入
    c1,c2,c3 = input().split()
    # 处理
    if c1 == c2 == c3:
        result = "Won"
    else:
        result = "Lost"
    # 输出结果
    print(result)
