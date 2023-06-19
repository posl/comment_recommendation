def main():
    #输入
    n = int(input())
    a = list(map(int, input().split()))
    #处理
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    #输出
    print(ans)
