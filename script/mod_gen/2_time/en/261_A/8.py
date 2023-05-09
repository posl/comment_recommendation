def main():
    # get input
    l1,r1,l2,r2 = map(int,input().split())
    # check if the parts are adjacent
    if r1 < l2:
        print(0)
    elif r2 < l1:
        print(0)
    elif r1 == l2:
        print(0)
    elif r2 == l1:
        print(0)
    else:
        # get the part painted both red and blue
        if l1 < l2:
            l = l2
        else:
            l = l1
        if r1 < r2:
            r = r1
        else:
            r = r2
        print(r-l)

if __name__ == '__main__':
    main()