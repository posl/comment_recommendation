def flip(n):
    return int(str(n).translate(str.maketrans('19', '91')))

if __name__ == '__main__':
    flip()