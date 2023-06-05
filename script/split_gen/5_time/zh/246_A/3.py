def problem246_a():
    x_1 = int(input('x_1:'))
    y_1 = int(input('y_1:'))
    x_2 = int(input('x_2:'))
    y_2 = int(input('y_2:'))
    x_3 = int(input('x_3:'))
    y_3 = int(input('y_3:'))
    if x_1 == x_2:
        x_4 = x_3
    elif x_1 == x_3:
        x_4 = x_2
    else:
        x_4 = x_1
    if y_1 == y_2:
        y_4 = y_3
    elif y_1 == y_3:
        y_4 = y_2
    else:
        y_4 = y_1
    print(x_4,y_4)
