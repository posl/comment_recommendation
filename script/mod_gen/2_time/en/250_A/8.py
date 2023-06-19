def check_square(x, y, h, w):
    if (x > 1 and y > 1) and (x < h and y < w):
        return 4
    elif (x > 1 and y > 1) or (x < h and y < w):
        return 3
    else:
        return 2
h, w = map(int, input().split())
r, c = map(int, input().split())
print(check_square(r, c, h, w))
