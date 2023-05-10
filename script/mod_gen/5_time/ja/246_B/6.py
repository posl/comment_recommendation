def main():
    a,b = map(int,input().split())
    c = (a**2+b**2)**0.5
    x = a/c
    y = b/c
    print(x,y)

if __name__ == '__main__':
    main()