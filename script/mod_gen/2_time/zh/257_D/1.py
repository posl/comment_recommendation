def isChild(W, S, X):
    if W < X and S == '0':
        return True
    elif W >= X and S == '1':
        return True
    else:
        return False

if __name__ == '__main__':
    isChild()