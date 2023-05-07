def main():
    x, y = input().split('.')
    if int(y) <= 2:
        print(x + '-')
    elif int(y) <= 6:
        print(x)
    else:
        print(x + '+')

if __name__ == '__main__':
    main()