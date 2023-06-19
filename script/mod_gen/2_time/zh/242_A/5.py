def main():
    a,b,c,x = map(int,input().split())
    if x <= a:
        print(1.0)
    elif x >= b+1:
        print(0.0)
    else:
        print(c/(b-a))

if __name__ == '__main__':
    main()