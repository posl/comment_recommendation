def count_odd_number(a_list):
    count = 0
    for a in a_list:
        if a % 2 == 1:
            count += 1
    return count
