def main():
    # 读入数据
    N, W = map(int, input().split())
    # print(N, W)
    # 读入N个人的计划
    # S:开始时间 T:结束时间 P:每分钟耗水量
    # 计划存储在列表中
    plan = []
    for i in range(N):
        S, T, P = map(int, input().split())
        plan.append([S, T, P])
    # print(plan)
    # 以开始时间为排序依据，升序排列
    plan.sort(key=lambda x: x[0])
    # print(plan)
    # 用一个列表存储每个人的耗水量
    water = [0] * N
    # print(water)
    # 用一个列表存储每个人的结束时间
    end_time = [0] * N
    # print(end_time)
    # 用一个列表存储每个人的开始时间
    start_time = [0] * N
    # print(start_time)
    # 用一个列表存储每个人的开始时间
    start_time = [0] * N
    # print(start_time)
    # 用一个列表存储每个人的耗水量
    water = [0] * N
    # print(water)
    # 用一个列表存储每个人的结束时间
    end_time = [0] * N
    # print(end_time)
    # 用一个列表存储每个人的开始时间
    start_time = [0] * N
    # print(start_time)
    # 用一个列表存储每个人的耗水量
    water = [0] * N
    # print(water)
    # 用一个列表存储每个人的结束时间
    end_time = [0] * N
    # print(end_time)
    # 用一个列表存储每个人的开始时间
    start_time = [0] * N
    # print(start_time)
    # 用一个列表存储每个人的耗水量
    water = [0] * N
    # print

if __name__ == '__main__':
    main()