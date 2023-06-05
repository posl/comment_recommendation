def rotate90(A):
    return list(zip(*A[::-1]))

if __name__ == '__main__':
    rotate90()