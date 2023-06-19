def get_count(h,w,r,c):
    count = 0
    if r == 1:
        if c == 1:
            count = 0
        elif c == w:
            count = 0
        else:
            count = 1
    elif r == h:
        if c == 1:
            count = 0
        elif c == w:
            count = 0
        else:
            count = 1
    else:
        if c == 1:
            count = 1
        elif c == w:
            count = 1
        else:
            count = 2
    return count

if __name__ == '__main__':
    get_count()