def main():
    # 读取输入
    s = input()
    # 计算
    ans = 0
    for i in range(len(s)):
        if i == 0:
            ans += (ord(s[i]) - ord('A')) + 1
        else:
            ans += (ord(s[i]) - ord('A')) * 26 ** i + 1
    # 输出
    print(ans)

if __name__ == '__main__':
    main()