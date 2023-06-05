def get_max_num(n, m, a):
    #n是火柴棒数，m是数字个数，a是数字列表
    #先根据a中的数字个数排序
    a.sort()
    a.reverse()
    #print(a)
    #计算每个数字需要的火柴棒数
    num_list = []
    for i in range(m):
        num_list.append(get_num(a[i]))
    #print(num_list)
    #计算最大数字
    max_num = ''
    while n > 0:
        for i in range(m):
            if n >= num_list[i]:
                max_num = max_num + str(a[i])
                n = n - num_list[i]
                break
    return max_num

if __name__ == '__main__':
    get_max_num()