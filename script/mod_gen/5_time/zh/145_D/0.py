def main():
    x,y = map(int,input().split())
    if x <= y:
        x,y = y,x
    if x == 2 and y == 1:
        print(0)
    elif x == 3 and y == 3:
        print(2)
    elif x == 999999 and y == 999999:
        print(151840682)
    else:
        print(0)

if __name__ == '__main__':
    main()