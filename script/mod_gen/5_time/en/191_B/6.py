def remove_element_from_list(list, element):
    while element in list:
        list.remove(element)
    return list

if __name__ == '__main__':
    remove_element_from_list()