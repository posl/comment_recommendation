def problems170_a(x):
    for i in range(5):
        if x[i] == 0:
            return i+1
    return -1
