def get_max_height_index(height_list):
    max_height = 0
    max_height_index = 0
    for i in range(len(height_list)):
        if height_list[i] > max_height:
            max_height = height_list[i]
            max_height_index = i
    return max_height_index
