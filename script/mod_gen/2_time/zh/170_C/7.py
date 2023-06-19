def get_closest_num(x, num_list):
    if len(num_list) == 0:
        return x
    else:
        min_diff = 100
        for num in num_list:
            if abs(num-x) < min_diff:
                min_diff = abs(num-x)
                closest_num = num
        return closest_num

if __name__ == '__main__':
    get_closest_num()