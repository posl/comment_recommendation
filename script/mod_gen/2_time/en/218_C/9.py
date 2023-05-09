def rotate(figure):
    return list(map(list,zip(*figure[::-1])))

if __name__ == '__main__':
    rotate()