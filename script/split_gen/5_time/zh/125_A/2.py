def problems125_a():
    a,b,t = [int(i) for i in input().split()]
    count = 0
    for i in range(1,t+1):
        if i%a == 0:
            count += b
    print(count)
