def get_slope(p1, p2):
    if p1[0] == p2[0]:
        return 0
    else:
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

if __name__ == '__main__':
    get_slope()