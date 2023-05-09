def main():
    w,h,x,y = map(int,input().split())
    area = w*h/2
    if w/2 == x and h/2 == y:
        print(area,1)
    else:
        print(area,0)

if __name__ == '__main__':
    main()