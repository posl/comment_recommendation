def main():
    x,y,n = map(int,input().split())
    if n%2==0:
        if x<y:
            print(x*(n//2))
        else:
            print(y*(n//2))
    else:
        if x<y:
            print(x*(n//2)+x)
        else:
            print(y*(n//2)+x)

if __name__ == '__main__':
    main()