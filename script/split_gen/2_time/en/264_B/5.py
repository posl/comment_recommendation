def get_color(row, col):
    if row % 2 == 0:
        if col % 2 == 0:
            return 'white'
        else:
            return 'black'
    else:
        if col % 2 == 0:
            return 'black'
        else:
            return 'white'
