def get_parent(x):
    if x % 2 == 0:
        return x // 2
    else:
        return (x + 1) // 2

if __name__ == '__main__':
    get_parent()