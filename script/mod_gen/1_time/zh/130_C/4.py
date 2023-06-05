def main():
    w,h,x,y = map(int,input().split())
    s = w*h/2
    if w/2 == x and h/2 == y:
        print(s,1)
    else:
        print(s,0)

if __name__ == '__main__':
    main()