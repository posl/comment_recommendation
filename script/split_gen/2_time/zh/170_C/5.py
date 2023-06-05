def check(x,y):
    for i in range(x+1):
        for j in range(x+1-i):
            if 2*i+4*j == y:
                return True
    return False
