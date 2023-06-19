def check_legs(x, y):
    if x == 2 * y or x == 4 * y:
        return True
    else:
        return False
x, y = map(int, input().split())

if __name__ == '__main__':
    check_legs()