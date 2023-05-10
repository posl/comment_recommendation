def main():
    x,y = map(int,input().split())
    if y%2 == 0:
        if (y-4*x) <= 0 and (y-2*x) >= 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()