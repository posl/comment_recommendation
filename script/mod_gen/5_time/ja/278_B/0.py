def main():
    h,m = map(int,input().split())
    if m == 0:
        if h == 23:
            h = 0
        else:
            h += 1
    else:
        m = 60 - m
        if h == 23:
            h = 0
        else:
            h += 1
    print(h,m)

if __name__ == '__main__':
    main()