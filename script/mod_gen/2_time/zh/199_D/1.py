def get_color_list(n):
    color_list = []
    for i in range(3**n):
        color_list.append(i)
    return color_list

if __name__ == '__main__':
    get_color_list()