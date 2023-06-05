def main():
    # 读取数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 执行操作
    for i in range(k):
        a.pop(0)
        a.append(0)
    # 打印结果
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()