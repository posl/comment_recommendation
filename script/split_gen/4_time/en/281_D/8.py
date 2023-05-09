def calc_sum(a_list, k, d):
    sum_list = []
    for i in range(0, len(a_list)):
        for j in range(i+1, len(a_list)):
            if len(sum_list) < k:
                sum_list.append(a_list[i] + a_list[j])
            else:
                break
    sum_list.sort(reverse=True)
    if len(sum_list) < k:
        return -1
    else:
        for s in sum_list:
            if s % d == 0:
                return s
        return -1
