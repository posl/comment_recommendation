def get_triangle_count(stick_list):
    triangle_count = 0
    stick_list.sort()
    for a_index in range(0, len(stick_list) - 2):
        for b_index in range(a_index + 1, len(stick_list) - 1):
            for c_index in range(b_index + 1, len(stick_list)):
                if stick_list[a_index] + stick_list[b_index] > stick_list[c_index]:
                    triangle_count += 1
    return triangle_count
