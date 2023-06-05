def isLunLun(x):
    if x < 10:
        return True
    else:
        x = str(x)
        for i in range(1, len(x)):
            if abs(int(x[i]) - int(x[i-1])) > 1:
                return False
        return True
