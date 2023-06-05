def find_max_num(n, m, a_list):
    #print(n, m, a_list)
    num_list = []
    for i in range(m):
        num_list.append(a_list[i])
    num_list.sort(reverse=True)
    #print(num_list)
    #print(num_list)
    max_num = ''
    for i in range(m):
        num = num_list[i]
        while n >= num:
            n = n - num
            max_num = max_num + str(num)
    return max_num

if __name__ == '__main__':
    find_max_num()