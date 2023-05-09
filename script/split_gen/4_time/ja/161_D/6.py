def is_rurun(x):
    if x < 10:
        return True
    x = str(x)
    for i in range(1,len(x)):
        if abs(int(x[i-1])-int(x[i])) > 1:
            return False
    return True
