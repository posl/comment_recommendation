def main():
    # 从标准输入读取字符串
    s = input()
    t = input()
    # 判断两个字符串是否相等
    if s == t:
        print('Yes')
        return
    # 循环判断s和t的字符是否相等
    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print('Yes')
            return
    print('No')
main()
