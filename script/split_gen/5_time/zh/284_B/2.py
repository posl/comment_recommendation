def count_odd_number(a_list):
    count = 0
    for i in a_list:
        if i % 2 != 0:
            count += 1
    return count
