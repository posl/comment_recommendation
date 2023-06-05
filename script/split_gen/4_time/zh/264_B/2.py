def print_color(row, col):
    if row % 2 == 0:
        if col % 2 == 0:
            print("白色")
        else:
            print("黑色")
    else:
        if col % 2 == 0:
            print("黑色")
        else:
            print("白色")
