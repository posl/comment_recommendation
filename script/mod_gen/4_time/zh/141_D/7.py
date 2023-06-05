def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 逐个处理
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        if a[0] < a[1]:
            a[0], a[1] = a[1], a[0]
    # 输出答案
    print(sum(a))

if __name__ == '__main__':
    main()