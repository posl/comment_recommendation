def main():
    # 读入数据
    n = int(input())
    x = list(map(int, input().split()))
    # 暴力解法
    # 从0到100中选择一个点，计算总体力
    # 选择总体力最小的点
    # 时间复杂度O(NM)，N为人数，M为坐标范围
    # ans = 10 ** 9
    # for i in range(101):
    #     tmp = 0
    #     for j in range(n):
    #         tmp += (x[j] - i) ** 2
    #     ans = min(ans, tmp)
    # print(ans)
    # 数学解法
    # 假设会议在坐标P举行
    # 第i个人将花费(X_i-P)^2点体力来参加会议
    # 求导，令导数为0，解出P
    # P = (X_1 + X_2 + ... + X_N) / N
    # 时间复杂度O(N)
    p = sum(x) // n
    ans = 0
    for i in range(n):
        ans += (x[i] - p) ** 2
    print(ans)

if __name__ == '__main__':
    main()