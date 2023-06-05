def get_color(r, c):
    if r % 2 == 0:
        if c % 2 == 0:
            return "black"
        else:
            return "white"
    else:
        if c % 2 == 0:
            return "white"
        else:
            return "black"
