def main():
    a,b = map(int, input().split())
    x = a/(a**2+b**2)**(1/2)
    y = b/(a**2+b**2)**(1/2)
    print(x,y)

if __name__ == '__main__':
    main()