def get_closest_number(x, p_list):
    closest_number = x
    diff = x
    for p in p_list:
        if abs(x - p) < diff:
            closest_number = p
            diff = abs(x - p)
    return closest_number

if __name__ == '__main__':
    get_closest_number()