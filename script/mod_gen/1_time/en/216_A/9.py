def main():
    #x, y = list(map(int, input().split('.')))
    #print(x, y)
    x, y = input().split('.')
    y = int(y)
    if y >= 0 and y <= 2:
        print(x + '-')
    elif y >= 3 and y <= 6:
        print(x)
    else:
        print(x + '+')

if __name__ == '__main__':
    main()