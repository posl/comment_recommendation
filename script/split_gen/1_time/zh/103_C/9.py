def get_max_mod_sum(a_list):
    a_list.sort()
    max_mod_sum = 0
    for i in range(1, a_list[-1]+1):
        mod_sum = 0
        for a in a_list:
            mod_sum += i % a
        if mod_sum > max_mod_sum:
            max_mod_sum = mod_sum
    return max_mod_sum
