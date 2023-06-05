def main():
    # 读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 判断是否可以升序排序
    for i in range(n - k):
        if a[i] > a[i + k]:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()