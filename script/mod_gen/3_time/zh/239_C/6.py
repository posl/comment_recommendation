def main():
    x1,y1,x2,y2 = map(int,input().split())
    if(x1 == x2 and y1 == y2):
        print('No')
        return
    if(x1 == x2):
        if(abs(y1-y2) == 5):
            print('Yes')
            return
        else:
            print('No')
            return
    if(y1 == y2):
        if(abs(x1-x2) == 5):
            print('Yes')
            return
        else:
            print('No')
            return
    if(abs(x1-x2) == 5 and abs(y1-y2) == 5):
        print('Yes')
        return
    else:
        print('No')
        return

if __name__ == '__main__':
    main()