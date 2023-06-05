def main():
    # 读取输入
    n = int(input())
    h = list(map(int, input().split()))
    # 从左到右，找到最后一个比左边高的平台
    ans = 0
    for i in range(n - 1):
        if h[i] < h[i + 1]:
            ans = h[i + 1]
    print(ans)

if __name__ == '__main__':
    main()