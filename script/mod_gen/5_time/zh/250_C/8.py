def main():
    # 读取数据
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    # 初始化
    a = [i for i in range(1, n+1)]
    # 交换
    for i in range(q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    # 输出
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()