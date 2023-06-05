def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 操作次数
    ans = 0
    # 遍历每个数
    for i in range(n):
        # 操作次数
        cnt = 0
        # 如果能整除2
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt += 1
        # 更新操作次数
        ans += cnt
    # 输出结果
    print(ans)
