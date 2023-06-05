def snow_depth(a,b):
    x = b - a
    return x * (x + 1) // 2 - a

if __name__ == '__main__':
    snow_depth()