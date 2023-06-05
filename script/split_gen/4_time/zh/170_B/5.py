def func(x, y):
    for i in range(x+1):
        if i*4+(x-i)*2 == y:
            return True
    return False
