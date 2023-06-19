def get_vertex(x1, y1, x2, y2, x3, y3):
    x4 = x3 + x1 - x2
    y4 = y3 + y1 - y2
    return x4, y4

if __name__ == '__main__':
    get_vertex()