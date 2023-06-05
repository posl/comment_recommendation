def main():
    # 读取输入
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 一开始的健康值
    health = H
    # 一开始的最小健康值
    min_health = health
    # 循环N次
    for i in range(N):
        # 健康值减少
        health -= A[i]
        # 如果健康值小于最小健康值
        if health < min_health:
            # 更新最小健康值
            min_health = health
    # 如果最小健康值小于等于0
    if min_health <= 0:
        # 打印Yes
        print('Yes')
    # 否则
    else:
        # 打印No
        print('No')
