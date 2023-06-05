def isLucky(x):
    x_str = str(x)
    for i in range(len(x_str)-1):
        if abs(int(x_str[i]) - int(x_str[i+1])) > 1:
            return False
    return True

if __name__ == '__main__':
    isLucky()