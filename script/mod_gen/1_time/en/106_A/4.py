def area():
    a = input()
    b = a.split()
    c = int(b[0])
    d = int(b[1])
    area = c*d
    return area

if __name__ == '__main__':
    area()