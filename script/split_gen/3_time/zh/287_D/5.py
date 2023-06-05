def main():
    # 读取输入
    s = input()
    t = input()
    # 计算匹配数
    count = 0
    for i in range(len(t)):
        if t[i] == '?':
            count += 1
    # 计算匹配结果
    for i in range(len(s) - len(t) + 1):
        flag = True
        for j in range(len(t)):
            if s[i + j] != t[j] and s[i + j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
