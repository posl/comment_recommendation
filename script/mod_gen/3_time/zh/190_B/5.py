def solve():
    # 读入N，S，D
    N, S, D = map(int, input().split())
    # 读入X_i, Y_i
    XY = [list(map(int, input().split())) for _ in range(N)]
    # 用于记录是否存在满足条件的法术
    flag = False
    # 遍历N个法术
    for i in range(N):
        # 如果存在满足条件的法术，跳出循环
        if flag:
            break
        # 如果第i个法术的施展时间小于S并且威力大于D，跳过
        if XY[i][0] < S and XY[i][1] > D:
            continue
        # 遍历N个法术
        for j in range(N):
            # 如果第j个法术的施展时间大于S或者威力小于D，跳过
            if XY[j][0] > S or XY[j][1] < D:
                continue
            # 如果第i个法术的施展时间小于等于第j个法术的施展时间并且威力大于等于第j个法术的威力，跳过
            if XY[i][0] <= XY[j][0] and XY[i][1] >= XY[j][1]:
                continue
            # 如果存在满足条件的法术，跳出循环
            if flag:
                break
            # 如果第i个法术的施展时间小于等于第j个法术的施展时间并且威力大于等于第j个法术的威力，跳出循环
            if XY[i][0] <= XY[j][0] and XY[i][1] >= XY[j][1]:
                break
        # 如果不存在满足条件的法术，跳出循环
        if j == N - 1:
            break
    # 如果存在满足条件的法术，打印Yes

if __name__ == '__main__':
    solve()