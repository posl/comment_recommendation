def lunlun(x):
    for i in range(len(x)-1):
        if abs(int(x[i+1])-int(x[i]))>1:
            return False
    return True

if __name__ == '__main__':
    lunlun()