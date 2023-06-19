def problem133_c(l,r):
    min = 2019
    for i in range(l,r):
        for j in range(i+1,r+1):
            if (i*j)%2019 < min:
                min = (i*j)%2019
    return min
