def main():
    n, k = map(int, input().split())
    t_d_list = [list(map(int, input().split())) for _ in range(n)]
    t_d_list.sort(key=lambda x: x[1], reverse=True)
    t_d_list.sort(key=lambda x: x[0])
    print(t_d_list)
    # 用于记录每种配料出现的次数
    t_list = [0] * n
    # 用于记录每种配料的最大美味值
    d_list = [0] * n
    for i in range(n):
        t_list[t_d_list[i][0]-1] += 1
        d_list[t_d_list[i][0]-1] = t_d_list[i][1]
    print(t_list)
    print(d_list)
    # 用于记录每种配料的美味值的最大k个值
    d_max_list = [0] * n
    for i in range(n):
        if t_list[i] != 0:
            d_max_list[i] = d_list[i]
    print(d_max_list)
    # 用于记录每种配料的美味值的最大k个值的和
    d_max_sum = sum(d_max_list)
    print(d_max_sum)
    # 用于记录每种配料的美味值的最大k个值的和的最大值
    d_max_sum_max = d_max_sum
    print(d_max_sum_max)
    # 用于记录每种配料的美味值的最大k个值的和的最大值的最大值
    d_max_sum_max_max = d_max_sum_max
    print(d_max_sum_max_max)
    # 用于记录每种配料的美味值的最大k个值的和的最大值的最大值的最大值
    d_max_sum_max_max_max = d_max_sum_max_max
    print(d_max_sum_max_max_max)
    # 用于记录每种配料的美味值的最大k个值的和的最大值的最大值的最大值的最大值
    d_max_sum_max_max_max_max = d_max_sum_max_max_max
    print(d_max_sum

if __name__ == '__main__':
    main()