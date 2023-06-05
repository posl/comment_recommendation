def main():
    r,c = map(int,input().split())
    if (r+c)%2 == 0:
        print('黑色')
    else:
        print('白色')

if __name__ == '__main__':
    main()