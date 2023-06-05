def sort_by_name(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j][0] > list[j+1][0]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
