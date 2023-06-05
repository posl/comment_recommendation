def get_point(x, y):
    for i in range(3):
        if x[i] == x[i-1]:
            x.append(x[i-2])
        elif x[i] == x[i-2]:
            x.append(x[i-1])
        else:
            x.append(x[i])
    for i in range(3):
        if y[i] == y[i-1]:
            y.append(y[i-2])
        elif y[i] == y[i-2]:
            y.append(y[i-1])
        else:
            y.append(y[i])
    return x[-1], y[-1]
