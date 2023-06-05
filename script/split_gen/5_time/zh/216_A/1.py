def main():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print('{}-'.format(x))
    elif 3 <= y <= 6:
        print(x)
    else:
        print('{}+'.format(x))
