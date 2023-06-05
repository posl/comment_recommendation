def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    #计算最少时间
    #最少时间是：最多人数／交通工具的最大载客量
    #最多人数是：n／交通工具的最少运行次数
    #交通工具的最少运行次数是：交通工具的最大载客量／交通工具的最少载客量
    #交通工具的最大载客量是：交通工具的最少载客量的整数倍（取整）
    #交通工具的最少载客量
    min_load = min(a,b,c,d,e)
    #交通工具的最大载客量
    max_load = max(a,b,c,d,e)
    #交通工具的最少运行次数
    min_run = int(max_load/min_load)
    #最多人数
    max_people = min_run*n
    #最少时间
    min_time = int(max_people/max_load)
    if max_people%max_load != 0:
        min_time += 1
    print(min_time)
