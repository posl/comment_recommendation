def mul_list(list):
    """
    :param list: list of integer
    :return: multiplication of the list
    """
    result = 1
    for i in range(len(list)):
        result = result * list[i]
    return result
