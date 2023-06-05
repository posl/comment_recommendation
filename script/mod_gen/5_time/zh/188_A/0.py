def check(X, Y):
    if X > Y:
        if X - Y < 3:
            return True
        else:
            return False
    else:
        if Y - X < 3:
            return True
        else:
            return False

if __name__ == '__main__':
    check()