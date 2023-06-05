def find_closest_num(target, num_list):
    num_list.sort()
    if target <= num_list[0]:
        return num_list[0]
    if target >= num_list[-1]:
        return num_list[-1]
    for i in range(len(num_list)-1):
        if num_list[i] <= target <= num_list[i+1]:
            return num_list[i] if abs(num_list[i]-target) <= abs(num_list[i+1]-target) else num_list[i+1]
