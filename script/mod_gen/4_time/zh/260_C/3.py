def main():
    n,x,y = map(int,input().split())
    if x > y:
        print(0)
    else:
        print((n-1)*x)

if __name__ == '__main__':
    main()