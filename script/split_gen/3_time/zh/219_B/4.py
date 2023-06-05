def main():
    # 读入数据
    s1 = input()
    s2 = input()
    s3 = input()
    T = input()
    # 处理并输出结果
    result = ''
    for i in range(len(T)):
        if T[i] == '1':
            result += s1
        elif T[i] == '2':
            result += s2
        else:
            result += s3
    print(result)
