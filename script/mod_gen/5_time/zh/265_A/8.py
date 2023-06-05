def main():
    x,y,n = map(int,input().split())
    print(x*(n//y)+x*(n%y>y//2))

if __name__ == '__main__':
    main()