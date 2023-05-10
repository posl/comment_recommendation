def check_honesty(x, y, honest):
    for i in range(len(x)):
        if y[i] == 1:
            if honest[x[i]-1] == 0:
                return 0
        else:
            if honest[x[i]-1] == 1:
                return 0
    return 1
