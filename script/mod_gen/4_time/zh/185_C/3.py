def cut(n):
    if n<2:
        return 1
    else:
        return cut(n-1)+n-1

if __name__ == '__main__':
    cut()