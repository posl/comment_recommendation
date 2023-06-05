def main():
    r,x,y = map(int,input().split())
    dis = (x**2 + y**2)**(1/2)
    if dis % r == 0:
        print(int(dis/r))
    elif dis < r:
        print(2)
    else:
        print(int(dis//r)+1)

if __name__ == '__main__':
    main()