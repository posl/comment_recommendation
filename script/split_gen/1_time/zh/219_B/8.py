def main():
    # 读入
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ""
    # 逐个字符读取t
    for i in t:
        if i == '1':
            result += s1
        elif i == '2':
            result += s2
        elif i == '3':
            result += s3
    # 打印结果
    print(result)
