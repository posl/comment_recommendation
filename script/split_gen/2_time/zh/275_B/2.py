def max_index(list):
    max = 0
    for i in range(1,len(list)):
        if list[i] > list[max]:
            max = i
    return max
