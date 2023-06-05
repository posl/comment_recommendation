def main():
    # 读入数据
    N, W = map(int, input().split())
    # 人员的使用时间和消耗量
    STP = []
    for n in range(N):
        s, t, p = map(int, input().split())
        STP.append([s, t, p])
    # 按照开始时间排序
    STP.sort(key=lambda x: x[0])
    # print(STP)
    # 每分钟的消耗量
    P = [0] * (2 * 10 ** 5 + 1)
    for s, t, p in STP:
        P[s] += p
        P[t] -= p
    # print(P)
    # 检查是否可以供应
    for i in range(2 * 10 ** 5):
        P[i + 1] += P[i]
        if P[i] > W:
            print("No")
            exit()
    print("Yes")
