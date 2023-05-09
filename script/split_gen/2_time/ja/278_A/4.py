def list_to_string(list):
    str = ""
    for i in range(len(list)):
        str += list[i]
        if i != len(list) - 1:
            str += " "
    return str
