def is9(n):
    s = sum([int(i) for i in str(n)])
    if s % 9 == 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    is9()