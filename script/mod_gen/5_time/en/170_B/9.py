def main():
    legs = 0
    legs = input().split()
    X = int(legs[0])
    Y = int(legs[1])
    if X*2 <= Y and X*4 >= Y and Y%2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()