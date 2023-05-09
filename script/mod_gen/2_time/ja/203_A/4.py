def main():
    a,b,c = map(int, input().split())
    if a==b and a==c:
        print(a)
    elif a==b:
        print(c)
    elif b==c:
        print(a)
    elif a==c:
        print(b)
    else:
        print(0)

if __name__ == '__main__':
    main()