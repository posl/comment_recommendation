def problems170_a(x):
    for i in range(len(x)):
        if x[i] == 0:
            return i+1
