def main():
    # 读取输入
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    # 计算结果
    result = ""
    for i in t:
        if i == '1':
            result += s1
        elif i == '2':
            result += s2
        else:
            result += s3
    # 打印结果
    print(result)
