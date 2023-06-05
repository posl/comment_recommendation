def main():
    # 读取输入
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    # 从1号房间开始，所以当前时间限制为T
    now = T
    # 遍历每个房间
    for i in range(N-1):
        # 消耗时间
        now -= A[i]
        # 如果时间到了，就返回No
        if now <= 0:
            print("No")
            return
        # 遍历奖励房间
        for j in range(M):
            # 如果当前房间是奖励房间，就增加时间
            if XY[j][0] == i + 1:
                now += XY[j][1]
    # 遍历完了，如果时间还有，就返回Yes
    if now > 0:
        print("Yes")
    else:
        print("No")
