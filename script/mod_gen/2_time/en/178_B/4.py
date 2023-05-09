def main():
    a,b,c,d = map(int,input().split())
    if a <= 0 and b >= 0:
        if c <= 0 and d >= 0:
            print(max(a*d,b*c))
        elif c > 0:
            print(b*c)
        elif d < 0:
            print(a*d)
    elif a > 0:
        print(b*c)
    elif b < 0:
        print(a*d)

if __name__ == '__main__':
    main()