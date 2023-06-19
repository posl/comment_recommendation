def solve(w):
    if w <= 3:
        print(3)
        print('1 2 3')
        return
    if w % 2 == 0:
        print(4)
        print('1 2 4 ' + str(w - 7))
        return
    print(5)
    print('1 2 4 ' + str(w - 7) + ' 7')
