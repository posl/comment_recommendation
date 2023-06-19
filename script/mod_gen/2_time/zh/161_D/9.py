def isLucky(x):
    s = str(x)
    for i in range(len(s)-1):
        if abs(int(s[i]) - int(s[i+1])) > 1:
            return False
    return True

if __name__ == '__main__':
    isLucky()