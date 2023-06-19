def main():
    w,h,x,y = map(int,input().split())
    print(w*h/2,end=' ')
    if w/2 == x and h/2 == y:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()