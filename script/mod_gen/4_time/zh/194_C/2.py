def main():
    #输入
    n = int(input())
    a = list(map(int, input().split()))
    #计算
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    #输出
    print(ans)

if __name__ == '__main__':
    main()