def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    if (x1+y1) == (x2+y2) or (x1-y1) == (x2-y2):
        print(1)
    elif abs(x1-x2)+abs(y1-y2) <= 3:
        print(1)
    elif (x1+y1)%2 == (x2+y2)%2:
        print(2)
    elif abs((x1+y1)-(x2+y2)) <= 3:
        print(2)
    elif abs((x1-y1)-(x2-y2)) <= 3:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    main()