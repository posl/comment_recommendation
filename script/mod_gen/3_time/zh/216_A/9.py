def main():
    input_str = input()
    x, y = input_str.split('.')
    y = int(y)
    if 0 <= y <= 2:
        print(x + '-')
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + '+')

if __name__ == '__main__':
    main()