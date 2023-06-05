def check(x,y):
    if y%2 == 0 and 2*x <= y and y <= 4*x:
        return True
    else:
        return False

if __name__ == '__main__':
    check()