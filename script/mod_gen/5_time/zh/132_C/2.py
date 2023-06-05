def main():
    # 读取数据
    n = int(input())
    d = list(map(int, input().split()))
    # 排序
    d.sort()
    # 确定K的范围
    # K的最小值为1，最大值为d[n//2]
    # K的取值范围是[1, d[n//2]]
    # 但是，如果d[n//2]是奇数，那么K的取值范围就是[1, d[n//2]+1]
    if d[n//2] % 2 == 0:
        k_min = 1
        k_max = d[n//2]
    else:
        k_min = 1
        k_max = d[n//2] + 1
    # 二分搜索
    # 二分搜索的判断条件是K的取值范围
    # 如果K的取值范围是[1, d[n//2]]，那么判断条件是k_max - k_min > 1
    # 如果K的取值范围是[1, d[n//2]+1]，那么判断条件是k_max - k_min > 0
    while k_max - k_min > 1:
        k = (k_min + k_max) // 2
        # 二分搜索的判断条件是ARC问题的数量和ABC问题的数量相同
        # 如果ARC问题的数量大于ABC问题的数量，那么K的取值范围是[k, k_max]
        # 如果ARC问题的数量小于ABC问题的数量，那么K的取值范围是[k_min, k]
        if sum(d[n//2:]) >= sum(d[n//2-k:]):
            k_min = k
        else:
            k_max = k
    # 打印结果
    print(k_min)

if __name__ == '__main__':
    main()