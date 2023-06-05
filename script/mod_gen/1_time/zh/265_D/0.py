def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    # 从左到右累积和
    for i in range(1, n):
        a[i] += a[i - 1]
    # 从右到左累积和
    for i in range(n - 2, -1, -1):
        a[i] += a[i + 1]
    # 检查是否存在满足条件的元组
    for i in range(n - 2):
        if a[i] >= p and a[i + 1] >= q and a[i + 2] >= r:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()