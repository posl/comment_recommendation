def find_closest_int(x, list_int):
    # x: integer
    # list_int: list of integers
    # return: integer
    # find the closest integer to x in list_int
    # if there are two integers with same distance to x, return the smaller one
    # if list_int is empty, return x
    if len(list_int) == 0:
        return x
    else:
        list_int = sorted(list_int)
        min_distance = abs(x - list_int[0])
        closest_int = list_int[0]
        for i in list_int:
            if abs(x - i) < min_distance:
                min_distance = abs(x - i)
                closest_int = i
        return closest_int

if __name__ == '__main__':
    find_closest_int()