def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 检查是否包含0
    if 0 in a:
        print(0)
        return
    # 计算答案
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10 ** 18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()