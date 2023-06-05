def get_num(x, y, a, b):
    return b//x - (a-1)//x + b//y - (a-1)//y - b//(x*y) + (a-1)//(x*y)
a, b, c, d = map(int, input().split())
print(get_num(c, d, a, b))
