def main():
    # input
    a,b,c = map(int, input().split())
    # compute
    # output
    if a==b:
        print(c)
    elif a==c:
        print(b)
    elif b==c:
        print(a)
    else:
        print(0)

if __name__ == '__main__':
    main()