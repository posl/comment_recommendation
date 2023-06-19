def check_inline (x1, y1, x2, y2, x3, y3):
    if (x1-x2)*(y2-y3) == (x2-x3)*(y1-y2):
        return True
    else:
        return False

if __name__ == '__main__':
    check_inline()