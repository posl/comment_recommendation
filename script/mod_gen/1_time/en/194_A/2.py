def get_category(a, b):
    if a + b >= 15 and b >= 8:
        return 1
    elif a + b >= 10 and b >= 3:
        return 2
    elif a + b >= 3:
        return 3
    else:
        return 4

if __name__ == '__main__':
    get_category()