def problem185_a():
    a = [int(i) for i in input().split()]
    a.sort()
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[0]+a[1]+a[2])
    print(a[0]+a[1]+a[3])
    print(a[0]+a[2]+a[3])
    print(a[1]+a[2]+a[3])
    print(a[0]+a[1]+a[2]+a[3])
    return
