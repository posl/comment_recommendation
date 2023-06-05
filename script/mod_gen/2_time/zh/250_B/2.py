def get_number_of_squares(h, w, r, c):
    if h == 1 and w == 1:
        return 0
    elif h == 1:
        return 1
    elif w == 1:
        return 1
    elif r == 1 and c == 1:
        return 0
    elif r == 1:
        return 1
    elif c == 1:
        return 1
    elif r == h and c == w:
        return 0
    elif r == h:
        return 1
    elif c == w:
        return 1
    else:
        return 2

if __name__ == '__main__':
    get_number_of_squares()