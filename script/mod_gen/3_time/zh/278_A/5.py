def main():
    #读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #执行K次操作
    for _ in range(k):
        a.append(0)
        a.pop(0)
    #打印结果
    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')

if __name__ == '__main__':
    main()