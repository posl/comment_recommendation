def main():
    # Read input
    x, y = input().split('.')
    y = int(y)
    
    # Check y
    if 0 <= y <= 2:
        print(x + '-')
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x + '+')
    else:
        print('Invalid input')

if __name__ == '__main__':
    main()