def print_x_y(x,y):
    if 0 <= y and y <= 2:
        print(x + "-")
    elif 3 <= y and y <= 6:
        print(x)
    elif 7 <= y and y <= 9:
        print(x + "+")

if __name__ == '__main__':
    print_x_y()