def main():
    # 读入数据
    N = int(input())
    a = list(map(int, input().split()))
    # 计算答案
    ans = 0
    for i in range(N):
        if a[i] - 1 == ans:
            ans += 1
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()