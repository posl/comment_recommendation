def answer(h,w,r,c):
    if r == 1 or r == h:
        if c == 1 or c == w:
            return 2
        else:
            return 3
    else:
        if c == 1 or c == w:
            return 3
        else:
            return 4
