def main():
    a,b = map(int,input().split())
    x = a/(a**2 + b**2)**0.5
    y = b/(a**2 + b**2)**0.5
    print(x,y)

if __name__ == '__main__':
    main()