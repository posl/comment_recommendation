def main():
    # 读入数据
    n = int(input())
    s = input()
    # 求解
    ans = 1
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            ans += 1
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()