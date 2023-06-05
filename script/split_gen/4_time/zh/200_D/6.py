def find_two_nums(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if i != j:
                if num_list[i] + num_list[j] == 200:
                    return num_list[i], num_list[j]
    return None, None
