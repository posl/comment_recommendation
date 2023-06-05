def problem180_d(x,y,a,b):
    exp = 0
    str = x
    while str < y:
        if str*a < str + b:
            str = str * a
            exp += 1
        else:
            str = str + b
            exp += 1
    print(exp)

if __name__ == '__main__':
    problem180_d()