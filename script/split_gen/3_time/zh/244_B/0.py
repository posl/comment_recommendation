def problems244_b():
    n = int(input())
    t = input()
    x = 0
    y = 0
    flag = 1
    for i in range(n):
        if t[i] == 'S':
            if flag == 1:
                x += 1
            elif flag == 2:
                y -= 1
            elif flag == 3:
                x -= 1
            elif flag == 4:
                y += 1
        elif t[i] == 'R':
            flag = (flag%4)+1
    print(x,y)
