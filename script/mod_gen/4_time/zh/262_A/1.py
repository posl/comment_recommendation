def sports(y):
    if y % 4 == 2:
        print(y)
    else:
        print(y + (2 - y % 4))

if __name__ == '__main__':
    sports()