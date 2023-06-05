def main():
    # 读取输入
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    # 逐个检查
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                ans += 1
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()