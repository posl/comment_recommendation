def find_min_diff(a_list, b_list):
    a_list.sort()
    b_list.sort()
    a_index = 0
    b_index = 0
    min_diff = abs(a_list[a_index] - b_list[b_index])
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] == b_list[b_index]:
            return 0
        elif a_list[a_index] < b_list[b_index]:
            a_index += 1
            min_diff = min(min_diff, abs(a_list[a_index] - b_list[b_index]))
        else:
            b_index += 1
            min_diff = min(min_diff, abs(a_list[a_index] - b_list[b_index]))
    return min_diff
