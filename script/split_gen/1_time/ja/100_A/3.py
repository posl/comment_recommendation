def main():
    a, b = map(int, input().split())
    if a+b > 16:
        print(':(')
    elif a > 8 or b > 8:
        print(':(')
    else:
        print('Yay!')
