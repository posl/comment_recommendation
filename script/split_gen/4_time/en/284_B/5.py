def count_odd(array):
    count = 0
    for i in array:
        if i % 2 == 1:
            count += 1
    return count
