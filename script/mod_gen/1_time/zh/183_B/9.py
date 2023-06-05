def main():
    x1,y1,x2,y2 = map(int,input().split())
    print((x1*y2-x2*y1)/(y2-y1))

if __name__ == '__main__':
    main()