def is753num(num):
    strnum = str(num)
    if strnum.count("7") > 0 and strnum.count("5") > 0 and strnum.count("3") > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is753num()