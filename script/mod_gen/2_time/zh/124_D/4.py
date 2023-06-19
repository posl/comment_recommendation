def main():
    # 读取输入
    n, k = map(int, input().split())
    s = input()
    # 初始化
    ans = 0
    # 从左到右遍历
    for i in range(n):
        # 如果当前是脚
        if s[i] == '0':
            # 如果是第一个
            if i == 0:
                # 如果后面是脚
                if s[i + 1] == '0':
                    # 翻转
                    ans += 1
            # 如果是最后一个
            elif i == n - 1:
                # 如果前面是脚
                if s[i - 1] == '0':
                    # 翻转
                    ans += 1
            # 如果是中间的
            else:
                # 如果前后都是脚
                if s[i - 1] == '0' and s[i + 1] == '0':
                    # 翻转
                    ans += 1
    # 如果翻转次数够
    if k <= ans:
        # 直接输出
        print(n)
        return
    # 如果翻转次数不够
    else:
        # 减去翻转次数
        ans = n - k
        # 输出
        print(ans)
        return

if __name__ == '__main__':
    main()