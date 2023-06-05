def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 生成b
    b = []
    for i in range(n):
        b.append(a[i])
    for i in range(n - 1):
        b.append(min(a[i], a[i + 1]))
    for i in range(n - 2):
        b.append(min(a[i], a[i + 1], a[i + 2]))
    for i in range(n - 3):
        b.append(min(a[i], a[i + 1], a[i + 2], a[i + 3]))
    for i in range(n - 4):
        b.append(min(a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4]))
    for i in range(n - 5):
        b.append(min(a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4], a[i + 5]))
    for i in range(n - 6):
        b.append(min(a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4], a[i + 5], a[i + 6]))
    for i in range(n - 7):
        b.append(min(a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4], a[i + 5], a[i + 6], a[i + 7]))
    for i in range(n - 8):
        b.append(min(a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4], a[i + 5], a[i + 6], a[i + 7], a[i + 8]))
    # 排序
    b.sort()
    # 打印结果
    print(b[n * (n + 1) // 2 - 1])

if __name__ == '__main__':
    main()