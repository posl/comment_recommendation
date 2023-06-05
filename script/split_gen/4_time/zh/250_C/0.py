def solve(n, q, x):
    #print("n=", n, "q=", q, "x=", x)
    #print("x=", x)
    for i in range(1, q+1):
        #print("i=", i)
        #print("x[i-1]=", x[i-1])
        if x[i-1] == i:
            #print("x[i-1]=", x[i-1], "i=", i)
            x[i-1], x[i] = x[i], x[i-1]
        else:
            #print("x[i-1]=", x[i-1], "i=", i)
            x[i-1], x[i] = x[i], x[i-1]
            x[i], x[i+1] = x[i+1], x[i]
    return x
