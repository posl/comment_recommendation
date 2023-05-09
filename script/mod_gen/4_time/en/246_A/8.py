def get_other_vertex(x1, y1, x2, y2, x3, y3):
    if x1 == x2:
        if y1 == y3:
            return x3, y2
        else:
            return x3, y1
    elif x1 == x3:
        if y1 == y2:
            return x2, y3
        else:
            return x2, y1
    else:
        if y1 == y2:
            return x1, y3
        else:
            return x1, y2

if __name__ == '__main__':
    get_other_vertex()