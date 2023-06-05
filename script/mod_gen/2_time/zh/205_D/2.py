def pow(x, y):
    if y == 0:
        return 1
    else:
        return x * pow(x, y-1)
A, B, C = map(int, input().split())

if __name__ == '__main__':
    pow()