def main():
    x = input().split('.')
    if 0 <= int(x[1]) <= 2:
        print(x[0] + '-')
    elif 3 <= int(x[1]) <= 6:
        print(x[0])
    else:
        print(x[0] + '+')

if __name__ == '__main__':
    main()