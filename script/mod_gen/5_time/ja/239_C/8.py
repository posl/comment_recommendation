def main():
    # input
    x1,y1,x2,y2 = map(int, input().split())
    # compute
    if (x1+x2+y1+y2)%2 == 0:
        if abs(x1-x2) == abs(y1-y2):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()