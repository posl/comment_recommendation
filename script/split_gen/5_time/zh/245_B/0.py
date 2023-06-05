def getMinNum(list):
    list.sort()
    if list[0] != 0:
        return 0
    else:
        for i in range(len(list)):
            if i == len(list) - 1:
                return list[i] + 1
            if list[i] + 1 != list[i + 1]:
                return list[i] + 1
