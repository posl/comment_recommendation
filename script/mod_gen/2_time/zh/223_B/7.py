def min_max_str(str):
    str_list = list(str)
    min_str = str
    max_str = str
    for i in range(len(str)):
        str_list.append(str_list.pop(0))
        str_temp = ''.join(str_list)
        if str_temp < min_str:
            min_str = str_temp
        if str_temp > max_str:
            max_str = str_temp
    return min_str, max_str

if __name__ == '__main__':
    min_max_str()