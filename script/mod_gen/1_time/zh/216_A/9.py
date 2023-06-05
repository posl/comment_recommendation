def main():
    x,y = map(float,input().split('.'))
    if 0<=y<=2:
        print(str(int(x))+'-')
    elif 3<=y<=6:
        print(str(int(x)))
    else:
        print(str(int(x))+'+')

if __name__ == '__main__':
    main()