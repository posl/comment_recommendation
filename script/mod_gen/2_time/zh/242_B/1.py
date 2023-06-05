def main():
    a,b,c,x = map(int,input().split())
    if a > x:
        print(0.0)
    elif a <= x <= b:
        print(1/c)
    else:
        print(0.0)

if __name__ == '__main__':
    main()