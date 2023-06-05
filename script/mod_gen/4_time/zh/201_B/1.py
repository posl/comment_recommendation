def get_second_height_mountain_name(mountain):
    mountain_list = mountain.split('\n')
    mountain_list = mountain_list[1:]
    mountain_list = [m.split(' ') for m in mountain_list]
    mountain_list = [[m[0], int(m[1])] for m in mountain_list]
    mountain_list.sort(key=lambda x: x[1], reverse=True)
    return mountain_list[1][0]

if __name__ == '__main__':
    get_second_height_mountain_name()