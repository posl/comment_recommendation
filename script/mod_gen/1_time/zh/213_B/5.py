def get_second_min(list):
    if len(list) < 2:
        return None
    min = list[0]
    second_min = None
    for i in range(1, len(list)):
        if list[i] < min:
            second_min = min
            min = list[i]
        elif list[i] != min and (second_min == None or list[i] < second_min):
            second_min = list[i]
    return second_min

if __name__ == '__main__':
    get_second_min()