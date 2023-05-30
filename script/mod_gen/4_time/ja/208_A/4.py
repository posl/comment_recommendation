def dice():
    a, b = map(int, input().split())
    if a <= 100 and b <= 1000:
        for i in range(1, a+1):
            for j in range(1, 7):
                if i * j == b:
                    print('Yes')
                    exit()
        print('No')
    else:
        print('No')
dice()
