def main():
    # 读取输入
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    # 初始化
    s = [k - q] * n
    # 逐个减分
    for i in a:
        s[i - 1] += 1
    # 输出
    for i in s:
        if i > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()