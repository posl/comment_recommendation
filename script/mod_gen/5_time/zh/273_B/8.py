def main():
    x,k = map(int,input().split())
    a = 10**k
    b = x // a
    c = (b+1) * a
    print(c)

if __name__ == '__main__':
    main()