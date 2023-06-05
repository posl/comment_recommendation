def find_missing_number(s):
    number_list = []
    for i in range(0,10):
        number_list.append(str(i))
    for i in s:
        if i in number_list:
            number_list.remove(i)
    return number_list[0]
