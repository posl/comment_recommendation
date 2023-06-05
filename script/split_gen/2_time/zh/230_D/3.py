def paint(a,b,n):
    #a,b表示起始点的坐标，n表示方块的大小
    for i in range(a,a+n):
        for j in range(b,b+n):
            if i+j == a+b+n-1:
                print('#',end='')
            else:
                print('.',end='')
        print()
