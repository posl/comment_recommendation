def main():
    x,y = map(float, input().split('.'))
    if y >= 0 and y <= 2:
        print(int(x)+'-')
    elif y >= 3 and y <= 6:
        print(int(x))
    elif y >= 7 and y <= 9:
        print(int(x)+'+')

if __name__ == '__main__':
    main()