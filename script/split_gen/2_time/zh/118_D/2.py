def find_max_num(n, m, a):
    a.sort()
    a.reverse()
    #print a
    max_num = 0
    max_num_list = []
    for i in range(0, m):
        if n > a[i]:
            max_num_list.append(a[i])
            n = n - a[i]
        elif n == a[i]:
            max_num_list.append(a[i])
            break
        else:
            continue
    #print max_num_list
    for j in range(0, len(max_num_list)):
        max_num = max_num * 10 + max_num_list[j]
    return max_num
