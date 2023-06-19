def main():
    # 读取输入
    s = input()
    t = input()
    # 从s中删除t中不存在的字符
    for i in range(len(t)):
        if t[i] not in s:
            print('No')
            return
        else:
            s = s[s.index(t[i])+1:]
    print('Yes')
    return

if __name__ == '__main__':
    main()