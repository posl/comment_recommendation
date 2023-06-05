def main():
    a,b,c,x = map(int, raw_input().split())
    if x <= a:
        print 1
    elif x >= b:
        print 0
    else:
        print float(c)/(b-a)

if __name__ == '__main__':
    main()