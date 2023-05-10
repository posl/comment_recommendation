def main():
    n, m = map(int, input().split())
    if m == 1:
        for i in range(n):
            for j in range(n):
                print(i+j)
            print()
        return
    elif m == 2:
        for i in range(n):
            for j in range(n):
                print(1 if (i+j)%2 else 0)
            print()
        return
    elif m == 3:
        for i in range(n):
            for j in range(n):
                print(i if (i+j)%3 == 0 else i+j)
            print()
        return
    elif m == 4:
        for i in range(n):
            for j in range(n):
                print((i//2+j//2)*2 if (i+j)%2 == 0 else (i+j)//2*2+1)
            print()
        return
    elif m == 5:
        for i in range(n):
            for j in range(n):
                print(i+j if (i+j)%5 == 0 else i+j+1)
            print()
        return
    else:
        for i in range(n):
            for j in range(n):
                print(i+j if (i+j)%7 == 0 else i+j+1)
            print()
        return

if __name__ == '__main__':
    main()