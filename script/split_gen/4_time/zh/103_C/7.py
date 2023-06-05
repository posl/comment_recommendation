def max_f(a_list):
    #a_list.sort()
    a_list.reverse()
    #print(a_list)
    max_f = 0
    for i in range(1, a_list[0]+1):
        f = 0
        for a in a_list:
            f += i % a
        if f > max_f:
            max_f = f
    return max_f
