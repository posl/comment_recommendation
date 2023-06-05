def max_difference(x):
    max = x[1]-x[0]
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if x[j]-x[i]>max:
                max = x[j]-x[i]
    return max
