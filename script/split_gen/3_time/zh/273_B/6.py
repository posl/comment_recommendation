def problem273_b(x, k):
    for i in range(k):
        x = int((x+5)/10)*10
    print(x)
