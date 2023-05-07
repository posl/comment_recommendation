def main():
    x = raw_input().split('.')
    y = int(x[1])
    if y <= 2:
        print x[0]+'-'
    elif y <= 6:
        print x[0]
    else:
        print x[0]+'+'

if __name__ == '__main__':
    main()