def main():
    a,b,c,d = map(int,input().split())
    if a > 0 and c > 0:
        print(max(a*c, a*d, b*c, b*d))
    elif a > 0 and d < 0:
        print(max(a*c, a*d, b*c, b*d))
    elif b < 0 and c > 0:
        print(max(a*c, a*d, b*c, b*d))
    elif b < 0 and d < 0:
        print(max(a*c, a*d, b*c, b*d))
    elif a > 0 and c <= 0 and d >= 0:
        print(max(a*c, a*d, b*c, b*d))
    elif b < 0 and c <= 0 and d >= 0:
        print(max(a*c, a*d, b*c, b*d))
    elif c > 0 and a <= 0 and b >= 0:
        print(max(a*c, a*d, b*c, b*d))
    elif d < 0 and a <= 0 and b >= 0:
        print(max(a*c, a*d, b*c, b*d))
    elif a <= 0 and b >= 0 and c <= 0 and d >= 0:
        print(max(a*c, a*d, b*c, b*d))
    else:
        print("Error")

if __name__ == '__main__':
    main()