def remove_element(list, element):
    for item in list:
        if item == element:
            list.remove(item)
    return list
