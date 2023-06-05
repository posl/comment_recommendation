def main():
    # 读入数据
    s = input()
    # 初始化变量
    ans = 0
    # 穷举
    for i in range(3):
        for j in range(i+1, 3):
            if s[i] != s[j]:
                ans += 1
    # 打印输出
    print(ans)

if __name__ == '__main__':
    main()