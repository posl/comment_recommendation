def count_odd(list):
    count = 0
    for i in list:
        if i % 2 != 0:
            count += 1
    return count
