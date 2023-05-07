def check(x,y,li):
    if x == 0 and y == 0:
        return True
    if x == 0:
        for i in range(len(li)):
            if li[i][1] == y:
                return True
    if y == 0:
        for i in range(len(li)):
            if li[i][0] == x:
                return True
    for i in range(len(li)):
        if li[i][0] == x and li[i][1] == y:
            return True
    return False

if __name__ == '__main__':
    check()