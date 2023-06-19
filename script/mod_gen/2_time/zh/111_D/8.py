def f():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        temp = input().split()
        x.append(int(temp[0]))
        y.append(int(temp[1]))
    if n == 1:
        print(-1)
        return
    if n == 2:
        if x[0] == x[1] and y[0] == y[1]:
            print(-1)
            return
        else:
            print(2)
            print(1, 1)
            print('LR')
            print('RL')
            return
    if n == 3:
        if x[0] == x[1] and x[1] == x[2]:
            print(2)
            print(1, 1)
            print('UDL')
            print('LDR')
            print('RUR')
            return
        if y[0] == y[1] and y[1] == y[2]:
            print(2)
            print(1, 1)
            print('LDR')
            print('RUR')
            print('UDL')
            return
        print(-1)
        return
    print(5)
    print(3, 1, 4, 1, 5)
    print('LRDUL')
    print('RDULR')
    print('DULRD')
    print('ULRDL')
    print('RDLRU')
    return
f()
