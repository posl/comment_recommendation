def main():
    # 读入数据
    n = int(input())
    x = list(map(int, input().split()))
    # 暴力解法
    # ans = 100000000000000000
    # for p in range(1, 101):
    #     sum = 0
    #     for i in range(n):
    #         sum += (x[i] - p) ** 2
    #     ans = min(ans, sum)
    # print(ans)
    # 优化解法
    ans = 100000000000000000
    for p in range(1, 101):
        sum = 0
        for i in range(n):
            sum += (x[i] - p) ** 2
        ans = min(ans, sum)
    print(ans)
