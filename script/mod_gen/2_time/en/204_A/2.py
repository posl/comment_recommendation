def main():
    x, y = input().split()
    if x == y:
        print(x)
    elif x == '0' and y == '1':
        print('2')
    elif x == '1' and y == '0':
        print('2')
    elif x == '1' and y == '2':
        print('0')
    elif x == '2' and y == '1':
        print('0')
    elif x == '2' and y == '0':
        print('1')
    elif x == '0' and y == '2':
        print('1')
    else:
        print('Error')

if __name__ == '__main__':
    main()