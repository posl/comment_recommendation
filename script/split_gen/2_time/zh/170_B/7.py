def problems170_b():
    x, y = map(int, input().split())
    for i in range(0, x + 1):
        for j in range(0, x + 1):
            if 2 * i + 4 * j == y and i + j == x:
                print('Yes')
                exit()
    print('No')
    exit()
