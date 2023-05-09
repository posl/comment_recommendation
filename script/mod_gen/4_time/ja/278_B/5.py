def main():
    h,m = map(int,input().split())
    if m < 59:
        m = m + 1
    else:
        m = 0
        if h < 23:
            h = h + 1
        else:
            h = 0
    print(h,m)

if __name__ == '__main__':
    main()