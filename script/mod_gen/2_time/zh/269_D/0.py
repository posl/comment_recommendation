def get_neighbour(x, y):
    if x % 2 == 0:
        return [(x-1, y-1), (x-1, y), (x, y-1), (x, y+1), (x+1, y), (x+1, y+1)]
    else:
        return [(x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y)]

if __name__ == '__main__':
    get_neighbour()