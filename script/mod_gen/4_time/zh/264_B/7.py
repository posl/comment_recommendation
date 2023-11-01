def get_color(row, col):
    if (row + col) % 2 == 0:
        return 'black'
    else:
        return 'white'

if __name__ == '__main__':
    get_color()