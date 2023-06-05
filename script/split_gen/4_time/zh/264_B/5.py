def main():
    R, C = map(int, input().split())
    if R % 2 == 0:
        if C % 2 == 0:
            print('白色')
        else:
            print('黑色')
    else:
        if C % 2 == 0:
            print('黑色')
        else:
            print('白色')
