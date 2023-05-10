def move(masu, koma):
    if masu[koma-1] == 1:
        masu[koma-1] = 0
        masu[koma] = 1
    return masu

if __name__ == '__main__':
    move()