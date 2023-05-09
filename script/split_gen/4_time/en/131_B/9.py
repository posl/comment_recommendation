def problem131_b():
    #print("Input the number of apples and the flavor of the first apple")
    n,l = map(int,input().split())
    #print("The number of apples is %d and the flavor of the first apple is %d" % (n,l))
    sum = 0
    min = 1000
    for i in range(n):
        sum += l+i
        if abs(l+i) < abs(min):
            min = l+i
    print(sum-min)
