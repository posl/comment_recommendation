def main():
    a,b = map(int,input().split())
    x = a/(a+b)
    y = b/(a+b)
    print(x,y)

if __name__ == '__main__':
    main()