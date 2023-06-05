def main():
    # 读取输入
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    # 处理并输出
    for i in range(len(t)):
        if t[i] == '1':
            print(s1, end='')
        elif t[i] == '2':
            print(s2, end='')
        elif t[i] == '3':
            print(s3, end='')
