def main():
    # 读入数据
    a1, a2, a3, a4 = map(int, input().split())
    # 计算可以举行的最大比赛数量
    print(min(a1, a2, a3, a4))
