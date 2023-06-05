def get_max_orange_number(orange_list):
    max_orange_number = 0
    for i in range(0, len(orange_list)):
        for j in range(i, len(orange_list)):
            for k in range(1, orange_list[j] + 1):
                if k > max_orange_number:
                    max_orange_number = k
    return max_orange_number
