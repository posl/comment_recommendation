def f(n, a):
    #从a中找出所有200的倍数，然后两两组合
    #找出所有200的倍数
    b = []
    for i in range(n):
        if a[i] % 200 == 0:
            b.append(i)
    #print(b)
    #两两组合
    count = 0
    for i in range(len(b)-1):
        for j in range(i+1, len(b)):
            count += 1
    return count
