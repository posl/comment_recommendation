def main():
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())
    r = abs(r1-r2)
    c = abs(c1-c2)
    if r == 0 and c == 0:
        print(0)
    elif r == c or r+c <= 3:
        print(1)
    elif (r+c)%2 == 0 or r+c <= 6 or abs(r-c) <= 3:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    main()