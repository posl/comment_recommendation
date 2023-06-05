def rotate90(arr):
    return list(zip(*arr[::-1]))

if __name__ == '__main__':
    rotate90()