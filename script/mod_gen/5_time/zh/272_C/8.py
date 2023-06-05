def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 检查是否有偶数
    for i in range(n):
        if a[i] % 2 == 0:
            print(a[i])
            return
    # 如果没有偶数，则检查是否有两个奇数之和为偶数
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 2 == 0:
                print(a[i] + a[j])
                return
    print(-1)

if __name__ == '__main__':
    main()