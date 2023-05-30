def oranges(a,b,w):
    min_oranges = 0
    max_oranges = 0
    for i in range(w*1000):
        if (i+1)*a <= w*1000 and (i+1)*b >= w*1000:
            min_oranges = i+1
        if (i+1)*a > w*1000:
            break
    for i in range(w*1000):
        if (i+1)*b >= w*1000:
            max_oranges = i+1
            break
    if min_oranges == 0 and max_oranges == 0:
        print("UNSATISFIABLE")
    else:
        print(min_oranges,max_oranges)
