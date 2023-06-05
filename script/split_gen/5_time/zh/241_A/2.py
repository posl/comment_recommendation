def problem241_a():
    a = input().split()
    for i in range(3):
        a = a[int(a[0])]
    print(a)
