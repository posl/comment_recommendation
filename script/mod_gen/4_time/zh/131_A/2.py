def main():
    # 读取输入
    s = input()
    # 初始化
    ans = 'Good'
    # 处理
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        ans = 'Bad'
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()