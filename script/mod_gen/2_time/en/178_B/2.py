def main():
    a,b,c,d = map(int,input().split())
    if b < 0 or d < 0:
        print(max(a*c,a*d,b*c,b*d))
    elif a > 0 or c > 0:
        print(max(a*c,a*d,b*c,b*d))
    else:
        print(max(a*c,b*d))

if __name__ == '__main__':
    main()