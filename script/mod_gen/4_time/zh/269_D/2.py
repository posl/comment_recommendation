def get_adjacent_list(x,y):
    adjacent_list = []
    adjacent_list.append((x-1,y-1))
    adjacent_list.append((x-1,y))
    adjacent_list.append((x,y-1))
    adjacent_list.append((x,y+1))
    adjacent_list.append((x+1,y))
    adjacent_list.append((x+1,y+1))
    return adjacent_list

if __name__ == '__main__':
    get_adjacent_list()